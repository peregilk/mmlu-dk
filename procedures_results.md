# Procedures and Resuls
Before runnign any of these commands you will need to optain an API key from [deepinfra.com](http://deepinfra.com). After that export the key as an environment variable.

```bash
export DEEPINFRA="<MY_KEY>"
```


# Translation Experiment

```bash
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations/DeepSeek-V3.jsonl --template_file templates/template.txt --model deepseek-ai/DeepSeek-V3
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations/Meta-Llama-3.1-405B-Instruct.jsonl --template_file templates/template.txt --model meta-llama/Meta-Llama-3.1-405B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations/Qwen2.5-72B-Instruct.jsonl --template_file templates/template.txt --model Qwen/Qwen2.5-72B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations/Mistral-Small-24B-Instruct-2501.jsonl --template_file templates/template.txt --model mistralai/Mistral-Small-24B-Instruct-2501
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations/Meta-Llama-3.1-8B-Instruct.jsonl --template_file templates/template.txt --model meta-llama/Meta-Llama-3.1-8B-Instruct
````
Result:
| Filename | N | 1 | 2 | 3 | 4 | 5 | Mean Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-V3 | 1000 | 0 | 0 | 1 | 16 | 983 | 4.98 |
| Meta-Llama-3.1-405B-Instruct | 1000 | 0 | 0 | 0 | 133 | 867 | 4.87 |
| Meta-Llama-3.1-8B-Instruct | 1000 | 0 | 0 | 79 | 358 | 563 | 4.48 |
| Mistral-Small-24B-Instruct-2501 | 1000 | 1 | 10 | 65 | 285 | 639 | 4.55 |
| Qwen2.5-72B-Instruct | 1000 | 0 | 1 | 4 | 112 | 883 | 4.88 |



# Comparisions


# Not really working yet....
```bash
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_100/DeepSeek-V3.jsonl --template_file templates/template_100.txt --model deepseek-ai/DeepSeek-V3

python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_100/Qwen2.5-72B-Instruct.jsonl --template_file templates/template_100.txt --model Qwen/Qwen2.5-72B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_100/Mistral-Small-24B-Instruct-2501.jsonl --template_file templates/template_100.txt --model mistralai/Mistral-Small-24B-Instruct-2501
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_100/Meta-Llama-3.1-8B-Instruct.jsonl --template_file templates/template_100.txt --model meta-llama/Meta-Llama-3.1-8B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_100/Meta-Llama-3.1-405B-Instruct.jsonl --template_file templates/template_100.txt --model meta-llama/Meta-Llama-3.1-405B-Instruct
```
I still get some errors here:

| Filename | N | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 | Mean Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-V3 | 1000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 127 | 0 | 0 | 41 | 4 | 828 | 99.28 |
| Meta-Llama-3.1-405B-Instruct | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 |
| Meta-Llama-3.1-8B-Instruct | 171 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 1 | 13 | 0 | 0 | 0 | 0 | 38 | 0 | 6 | 0 | 0 | 67 | 0 | 1 | 10 | 0 | 23 | 92.42 |
| Mistral-Small-24B-Instruct-2501 | 1000 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 12 | 0 | 2 | 1 | 1 | 14 | 0 | 0 | 2 | 2 | 13 | 0 | 0 | 2 | 0 | 41 | 3 | 2 | 6 | 5 | 44 | 1 | 3 | 1 | 2 | 183 | 5 | 12 | 6 | 4 | 146 | 0 | 6 | 3 | 1 | 263 | 4 | 10 | 37 | 25 | 122 | 88.85 |
| Qwen2.5-72B-Instruct | 1000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 5 | 0 | 63 | 0 | 1 | 0 | 0 | 11 | 0 | 35 | 8 | 4 | 518 | 1 | 7 | 40 | 1 | 283 | 95.09 |


Some lines might not have given a valid output here, so you might have to rerun the script. If you rerun a completed file, the script will automatically enter repair mode.




# Download the alexndria dataset. Then adapt it
```bash
jq 'with_entries(if .key == "instruction" then .key = "question" else . end)' -c dev_alexandria.jsonl > temp.jsonl && mv temp.jsonl dev_alexndria.jsonl
jq 'with_entries(if .key == "instruction" then .key = "question" else . end)' -c en.jsonl > temp.jsonl && mv temp.jsonl en.jsonl
jq 'with_entries(if .key == "id" then .key = "sample_id" else . end)' -c dev_alexandria.jsonl > temp.jsonl && mv temp.jsonl dev_alexandria.jsonl
jq 'with_entries(if .key == "id" then .key = "sample_id" else . end)' -c en.jsonl > temp.jsonl && mv temp.jsonl en.jsonl
```

# Compare models
```bash
bash run_comparison.sh
bash run_alexandria_comparison.sh
```

# Find Best Scores
```bash
python mmlu_find_best_scores.py --input_folder experiment_compare/ --output_file experiment_compare/comparison_BestModelWithoutSmall_by_BestModelWithoutSmall.jsonl --exclude_reasoning --exclude_smallmodels
python mmlu_find_best_scores.py --input_folder experiment_compare/ --output_file experiment_compare/comparison_BestModelWithoutReasoning_by_BestModelWithoutReasoning.jsonl --exclude_reasoning
python mmlu_find_best_scores.py --input_folder experiment_compare/ --output_file experiment_compare/comparison_BestModel_by_BestModel.jsonl
```

# Create MarkDown
```bash
python mmlu_analyse_comparisons.py
```

# Cost Estimates
```bash
# Transltion
DeepSeek-R1 - 285 examples = $1.34182635 -> $65.913 for 14k
DeepSeek-V3 - 285 examples = $0.30226221 -> $14.848 for 14k
Llama_3.1-405B - 285 examples = $0.43798800 -> $21.515 for 14k
Llama_3.3-70B - 285 examples = $0.14283057 -> $7.016 for 14k

# Comparisons - needs to be multiplied by N
DeepSeek-R1 - 285 examples = $0.91000590 -> $44.702 for 14k
DeepSeek-V3 - 285 examples - $0.08400600 -> $4.127
Llama_3.1-405B - 285 examples = $0.17398000 -> $8.564 for 14k
Llama_3.3-70B - 285 examples = $0.05175618 -> $2.542 for 14k
```

## Prices
| Model            | Translation | Comparison |
|-----------------|------------|------------|
| DeepSeek R1     | $66        | $44        |
| DeepSeek V3     | $15        | $4         |
| Llama 3.1 405B  | $21        | $9         |
| Llama 3.3 70B   | $7         | $3         |


## Experiment Cost
| Model                                      | Calculation                                                    | Cost  | Comment      |
|--------------------------------------------|----------------------------------------------------------------|-------|--------------|
| R1                                         | -                                                              | $66   |OK            |
| V3-405B-70B-comparison                     | ($15 + $21 + $7) + (3 × $4 + 3 × $9 + 3 × $3)                  | $91   |OK            |
| R1-V3-405B-70B-comparison                  | ($66 + $15 + $21 + $7) + (4 × $44 + 4 × $4 + 4 × $9 + 4 × $3)  | $349  |Too expensive |
| V3                                         | $15 but included above                                         | $0    |OK            |
| Alexandra Institute external               | external                                                       | $0    |OK            |




