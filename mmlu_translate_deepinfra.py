#!/usr/bin/env python3
import os
import json
import argparse
import re
import threading
import logging
from openai import OpenAI
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

# Global cost tracking
total_cost = 0.0
cost_lock = threading.Lock()

# Thread-local storage for the API client
_thread_local = threading.local()


def get_client(api_key):
    if not hasattr(_thread_local, "client"):
        _thread_local.client = OpenAI(api_key=api_key, base_url="https://api.deepinfra.com/v1/openai")
    return _thread_local.client


def accumulate_stream_response(response):
    """
    Gathers streamed chunks and returns a single string.
    """
    full_text = ""
    for chunk in response:
        delta = chunk.choices[0].delta
        full_text += delta.get("content", "")
    return full_text.strip(), ""


def parse_api_response(text):
    """
    Attempt to extract a JSON object from the first '{' to the last '}'.
    """
    text = text.strip()
    # Remove <think> blocks
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    # Remove markdown fences
    if text.startswith("```"):
        text = text.strip("`").strip()

    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        json_text = text[start:end + 1]
        return json.loads(json_text)

    raise ValueError("No valid JSON object found in text.")


def process_record(line, template, api_key, stream_output, model):
    """
    Processes a single JSON line => returns a JSON string.
    If error occurs, returns an error record with "Score":0 for later repair.
    """
    global total_cost
    try:
        input_data = json.loads(line.strip())
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding failed: {line.strip()} | {e}")
        return None

    required_keys = [
        "sample_id", "subject", "subject_category", "question",
        "option_a", "option_b", "option_c", "option_d", "answer",
        "required_knowledge", "time_sensitive", "reference", "culture",
        "region", "country", "cultural_sensitivity_label", "is_annotated"
    ]
    for rk in required_keys:
        if rk not in input_data:
            logging.warning(f"Skipping because missing {rk}: {input_data}")
            return None

    to_translate = {
        "question": input_data["question"],
        "option_a": input_data["option_a"],
        "option_b": input_data["option_b"],
        "option_c": input_data["option_c"],
        "option_d": input_data["option_d"],
    }
    user_prompt = template.replace("{question}", json.dumps(to_translate, ensure_ascii=False))

    client = get_client(api_key)

    error_reason = None
    try:
        error_reason = "API call failed"
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": user_prompt},
            ],
            stream=stream_output,
            max_tokens=8192,
        )

        if stream_output:
            final_text, _ = accumulate_stream_response(response)
        else:
            message = response.choices[0].message
            final_text = message.content.strip() if message.content else ""

        # Grab usage cost if present
        cost_val = getattr(response.usage, "estimated_cost", 0.0) if hasattr(response, "usage") else 0.0
        with cost_lock:
            total_cost += cost_val

        error_reason = "Not valid JSON"
        output_data = parse_api_response(final_text)

        # Merge data
        final_out = {}
        for k in required_keys:
            if k in to_translate:
                final_out[k] = output_data.get(k, "N/A")
            else:
                final_out[k] = input_data.get(k, "N/A")

        # Include extra keys from the model
        for k in output_data:
            if k not in final_out:
                final_out[k] = output_data[k]

    except Exception as e:
        logging.error(f"Processing error: {e} - reason: {error_reason}")
        # Return an error record
        fail_out = {rk: input_data.get(rk, "N/A") for rk in required_keys}
        fail_out["Reason"] = str(error_reason)
        fail_out["Score"] = 0  # triggers repair
        return json.dumps(fail_out, ensure_ascii=False)

    return json.dumps(final_out, ensure_ascii=False)


def process_file_parallel(
    input_file,
    template,
    output_file,
    api_key,
    stream_output,
    num_workers,
    write_immediately,
    model,
    max_items=None
):
    """
    Reads all lines in 'input_file'.
    Skips lines that are already in 'output_file' (by count).
    Then processes up to 'max_items' from the remainder.
    Appends them to 'output_file'.
    Returns the number of lines actually processed in this pass.
    """
    out_count = 0
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f_out:
            out_count = sum(1 for _ in f_out)

    with open(input_file, "r", encoding="utf-8") as f_in:
        in_lines = f_in.readlines()
    total_in = len(in_lines)

    # Lines that remain to be processed
    remain = total_in - out_count
    if remain <= 0:
        logging.info("No new lines to process (out_count >= total_in).")
        return 0  # no new lines processed

    # If a max_items is set, we only do that many
    to_do = remain
    if max_items is not None and out_count < max_items:
        # We only process until we reach max_items
        # E.g. if out_count=200 and max_items=1000 => we can process up to 800 new lines in this run
        to_do = min(to_do, (max_items - out_count))

    if to_do <= 0:
        # Means we've already reached or exceeded max_items => no partial processing
        logging.info("We have reached or exceeded the max_items threshold, skipping partial processing.")
        return 0

    lines_to_process = in_lines[out_count:out_count + to_do]
    logging.info(f"Processing {len(lines_to_process)} lines (from {out_count} to {out_count + to_do}).")

    with ThreadPoolExecutor(max_workers=num_workers) as executor, \
            open(output_file, "a", encoding="utf-8") as out_f:

        for processed in tqdm(
            executor.map(
                process_record,
                lines_to_process,
                repeat(template),
                repeat(api_key),
                repeat(stream_output),
                repeat(model)
            ),
            total=len(lines_to_process),
            desc="Processing"
        ):
            if processed is not None:
                if write_immediately:
                    out_f.write(processed + "\n")
                    out_f.flush()
                else:
                    # If you had buffering, you'd store them first
                    out_f.write(processed + "\n")

    return len(lines_to_process)


def repair_file(
    input_file,
    output_file,
    template,
    api_key,
    stream_output,
    num_workers,
    model
):
    """
    Reads 'output_file' line by line. For each line up to min(len(input),len(output)):
      - If parse fails or 'Score' is not an int 1..100 => reprocess that line from the input.
    Overwrites output_file with the result.
    """
    if not os.path.exists(output_file):
        logging.warning("No output file found; nothing to repair.")
        return

    with open(input_file, "r", encoding="utf-8") as f_in:
        in_lines = f_in.readlines()
    with open(output_file, "r", encoding="utf-8") as f_out:
        out_lines = f_out.readlines()

    min_len = min(len(in_lines), len(out_lines))
    fixed_output = [None] * min_len
    reproc_indices = []

    # Identify lines that need reprocessing
    for idx in range(min_len):
        old_line = out_lines[idx].strip()
        try:
            data = json.loads(old_line)
            # unify Score vs score
            scr = data.get("Score", data.get("score"))
            if not (isinstance(scr, int) and 1 <= scr <= 100):
                reproc_indices.append(idx)
            else:
                fixed_output[idx] = old_line
        except json.JSONDecodeError:
            reproc_indices.append(idx)

    reproc_input = [in_lines[i] for i in reproc_indices]

    # Reprocess
    results_map = {}
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_map = {
            executor.submit(
                process_record,
                reproc_input[i],
                template,
                api_key,
                stream_output,
                model
            ): reproc_indices[i]
            for i in range(len(reproc_indices))
        }
        for fut in tqdm(future_map, total=len(reproc_indices), desc="Repairing"):
            idx = future_map[fut]
            try:
                res = fut.result()
                if res is not None:
                    results_map[idx] = res.strip()
                else:
                    # fallback
                    results_map[idx] = out_lines[idx].strip()
            except Exception as e:
                logging.error(f"Repair error at line {idx}: {e}")
                results_map[idx] = out_lines[idx].strip()

    for idx in reproc_indices:
        fixed_output[idx] = results_map[idx]

    # If output had leftover lines beyond min_len, keep them
    if len(out_lines) > min_len:
        leftover = out_lines[min_len:]
        fixed_output.extend(line.strip() for line in leftover)

    # Write final
    with open(output_file, "w", encoding="utf-8") as f_out:
        for line in fixed_output:
            f_out.write(line + "\n")

    logging.info(f"Repaired {len(reproc_indices)} lines in total.")


def load_template(tpath):
    with open(tpath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description="Process partial lines or auto-repair based on max_items or total_in.")
    parser.add_argument("--input_file", required=True, help="Input JSON lines.")
    parser.add_argument("--template_file", required=True, help="Template file.")
    parser.add_argument("--output_file", required=True, help="Output file.")
    parser.add_argument("--processes", type=int, default=50, help="Number of parallel workers.")
    parser.add_argument("--model", default="deepseek-ai/DeepSeek-R1", help="Model to use.")
    parser.add_argument("--max_items", type=int, default=None, help="Stop normal processing once output lines >= this.")
    parser.add_argument("--debug", action="store_true", help="Enable debug logs.")
    args = parser.parse_args()

    # Logging setup
    lvl = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=lvl, format='%(asctime)s - %(levelname)s - %(message)s')

    # Validate API key
    api_key = os.getenv("DEEP_INFRA")
    if not api_key:
        raise EnvironmentError("DEEP_INFRA environment variable not set.")

    # Ensure output directory
    odir = os.path.dirname(args.output_file)
    if odir:
        os.makedirs(odir, exist_ok=True)

    template_content = load_template(args.template_file)

    # Count how many lines are currently in output (if file exists)
    out_count = 0
    if os.path.exists(args.output_file):
        with open(args.output_file, "r", encoding="utf-8") as f_out:
            out_count = sum(1 for _ in f_out)
    logging.info(f"Currently {out_count} lines in output.")

    # Count total lines in input
    with open(args.input_file, "r", encoding="utf-8") as f_in:
        total_in = sum(1 for _ in f_in)
    logging.info(f"Total lines in input: {total_in}.")

    # Decide whether to do partial processing or auto-repair:
    # Condition: if out_count < total_in and out_count < max_items => partial
    # Otherwise => repair
    # (If max_items not given, that part is ignored in the check.)

    must_repair = False
    if out_count < total_in:
        # We do have lines left to process from input
        if args.max_items is not None:
            # We only do partial if out_count < max_items
            if out_count >= args.max_items:
                must_repair = True
            else:
                # do partial processing
                processed_now = process_file_parallel(
                    input_file=args.input_file,
                    template=template_content,
                    output_file=args.output_file,
                    api_key=api_key,
                    stream_output=False,
                    num_workers=args.processes,
                    write_immediately=True,
                    model=args.model,
                    max_items=args.max_items
                )
                if processed_now == False:
                    logging.info("No new lines processed. Possibly everything is up to date. Skipping repair.")
        else:
            # no max_items => just partial process everything left
            processed_now = process_file_parallel(
                input_file=args.input_file,
                template=template_content,
                output_file=args.output_file,
                api_key=api_key,
                stream_output=False,
                num_workers=args.processes,
                write_immediately=True,
                model=args.model,
                max_items=None
            )
            if processed_now == False:
                logging.info("No new lines processed. Possibly everything is up to date.")
    else:
        # output_count >= total_in => no new lines => must repair
        must_repair = True

    # If the logic concluded we must repair:
    if must_repair:
        logging.info("Auto-detected repair mode: output_count >= max_items or >= total_in.")
        repair_file(
            input_file=args.input_file,
            output_file=args.output_file,
            template=template_content,
            api_key=api_key,
            stream_output=False,
            num_workers=args.processes,
            model=args.model
        )

    print(f"Total estimated cost: {total_cost:.8f}")


if __name__ == "__main__":
    main()