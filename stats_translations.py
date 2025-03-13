#!/usr/bin/env python3
import os
import json
import argparse
from collections import Counter
from statistics import mean

def process_file(file_path, max_score):
    """
    Reads a JSON-lines file and computes frequency counts for scores 1 through max_score,
    as well as the mean score.
    """
    scores = []
    counter = Counter()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            score = record.get("score")
            if score is not None:
                try:
                    score_int = int(score)
                    if 1 <= score_int <= max_score:
                        scores.append(score_int)
                        counter[score_int] += 1
                except ValueError:
                    # score is not an integer, ignore
                    continue

    avg_score = mean(scores) if scores else 0
    # Ensure counts for all scores 1 to max_score are present
    counts = {i: counter.get(i, 0) for i in range(1, max_score + 1)}
    # N = total valid scores in the 1..max_score range
    n_valid_scores = sum(counts.values())
    return counts, avg_score, n_valid_scores

def main():
    parser = argparse.ArgumentParser(
        description="Compute score stats from JSON-lines files in a target directory."
    )
    parser.add_argument(
        "--target_directory",
        default="translations",
        help="Directory containing JSON-lines files (default: translations)"
    )
    parser.add_argument(
        "--max_score",
        type=int,
        default=5,
        help="Maximum possible score (default: 5). For instance, if set to 100, "
             "we will show frequency counts for 1..100."
    )
    args = parser.parse_args()

    target_dir = args.target_directory
    max_score = args.max_score

    if not os.path.exists(target_dir):
        print(f"Directory '{target_dir}' does not exist.")
        return

    # Collect all JSON lines files (only files, not subdirectories)
    files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]

    # Prepare Markdown table header
    # Example columns: | Filename | N | 1 | 2 | ... | max_score | Mean Score |
    score_columns = " | ".join(str(i) for i in range(1, max_score + 1))
    header = f"| Filename | N | {score_columns} | Mean Score |"
    separator = "| --- | --- | " + " | ".join(["---"] * max_score) + " | --- |"

    table_lines = [header, separator]

    for file_name in sorted(files):
        file_path = os.path.join(target_dir, file_name)
        counts, avg_score, n_valid_scores = process_file(file_path, max_score)
        display_name = file_name[:-6] if file_name.endswith(".jsonl") else file_name

        # Create row with frequency counts for each score
        score_counts_str = " | ".join(str(counts[i]) for i in range(1, max_score + 1))
        row = (
            f"| {display_name} | {n_valid_scores} | {score_counts_str} | {avg_score:.2f} |"
        )
        table_lines.append(row)

    # Print the Markdown table
    print("\n".join(table_lines))

if __name__ == "__main__":
    main()