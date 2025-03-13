#!/bin/bash


models=("deepseek-ai/DeepSeek-V3" "meta-llama/Meta-Llama-3.1-405B-Instruct" "Qwen/Qwen2.5-72B-Instruct" "mistralai/Mistral-Small-24B-Instruct-2501" "meta-llama/Meta-Llama-3.1-8B-Instruct")
translated_files=("DeepSeek-V3.jsonl"  "Meta-Llama-3.1-405B-Instruct.jsonl" "Qwen2.5-72B-Instruct.jsonl" "Mistral-Small-24B-Instruct-2501.jsonl" "Meta-Llama-3.1-8B-Instruct.jsonl"  )


for model in "${models[@]}"; do
    model_name=$(echo "$model" | sed 's|.*/||')  # Extract model name after last "/"
    for translated_file in "${translated_files[@]}"; do
        translated_model_name=$(echo "$translated_file" | sed 's/^test_//' | sed 's/\.jsonl$//')
        output_file="comparisons/comparison_${translated_model_name}_by_${model_name}.jsonl"
        echo "Running comparison: Model=$model, Translated file=$translated_file"
        python mmlu_comparison_deepinfra.py --english_file mmlu_download/Global-MMLU_test_en.jsonl --german_file translations/${translated_file} --output_file ${output_file} --model ${model}
    done
done
