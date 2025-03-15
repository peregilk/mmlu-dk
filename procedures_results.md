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
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations/Llama-3.2-1B-Instruct.jsonl --template_file templates/template.txt --model meta-llama/Llama-3.2-1B-Instruct

````
Result:
| Filename | N | 1 | 2 | 3 | 4 | 5 | Mean Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-V3 | 1000 | 0 | 0 | 1 | 16 | 983 | 4.98 |
| Llama-3.2-1B-Instruct | 1000 | 74 | 237 | 248 | 403 | 38 | 3.09 |
| Meta-Llama-3.1-405B-Instruct | 1000 | 0 | 0 | 0 | 133 | 867 | 4.87 |
| Meta-Llama-3.1-8B-Instruct | 1000 | 0 | 0 | 79 | 358 | 563 | 4.48 |
| Mistral-Small-24B-Instruct-2501 | 1000 | 1 | 10 | 65 | 285 | 639 | 4.55 |
| Qwen2.5-72B-Instruct | 1000 | 0 | 1 | 4 | 112 | 883 | 4.88 |


# Translation Performance

```bash
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_performance/DeepSeek-V3.jsonl --template_file templates/template_performance.txt --model deepseek-ai/DeepSeek-V3
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_performance/Meta-Llama-3.1-405B-Instruct.jsonl --template_file templates/template_performance.txt --model meta-llama/Meta-Llama-3.1-405B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_performance/Qwen2.5-72B-Instruct.jsonl --template_file templates/template_performance.txt --model Qwen/Qwen2.5-72B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_performance/Mistral-Small-24B-Instruct-2501.jsonl --template_file templates/template_performance.txt --model mistralai/Mistral-Small-24B-Instruct-2501
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_performance/Meta-Llama-3.1-8B-Instruct.jsonl --template_file templates/template_performance.txt --model meta-llama/Meta-Llama-3.1-8B-Instruct
python mmlu_translate_deepinfra.py --max_items 1000 --input_file mmlu_download/Global-MMLU_test_en.jsonl --output_file translations_performance/Llama-3.2-1B-Instruct.jsonl --template_file templates/template_performance.txt --model meta-llama/Llama-3.2-1B-Instruct

````
Result:
| Filename | N | 1 | 2 | 3 | 4 | 5 | Mean Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-V3 | 1000 | 0 | 0 | 0 | 99 | 901 | 4.90 |
| Llama-3.2-1B-Instruct | 997 | 31 | 187 | 253 | 478 | 48 | 3.33 |
| Meta-Llama-3.1-405B-Instruct | 1000 | 0 | 0 | 2 | 595 | 403 | 4.40 |
| Meta-Llama-3.1-8B-Instruct | 1000 | 0 | 3 | 156 | 577 | 264 | 4.10 |
| Mistral-Small-24B-Instruct-2501 | 1000 | 0 | 4 | 62 | 515 | 419 | 4.35 |
| Qwen2.5-72B-Instruct | 1000 | 0 | 1 | 8 | 506 | 485 | 4.47 |


# Comparisions
The `mmlu_comparisons_deepinfra.py`is run by the command `bash run_comparisons.sh`.

After that we can run `python stats_comparisons.py`

It produces these results:
### Translation Quality Table
|                                 |   DeepSeek-V3 |   Meta-Llama-3.1-405B-Instruct |   Meta-Llama-3.1-8B-Instruct |   Mistral-Small-24B-Instruct-2501 |   Qwen2.5-72B-Instruct |
|:--------------------------------|--------------:|-------------------------------:|-----------------------------:|----------------------------------:|-----------------------:|
| DeepSeek-V3                     |          4.93 |                           4.97 |                         4.13 |                              4.7  |                   4.79 |
| Meta-Llama-3.1-405B-Instruct    |          4.88 |                           4.98 |                         4.12 |                              4.64 |                   4.75 |
| Meta-Llama-3.1-8B-Instruct      |          4.22 |                           4.71 |                         4.11 |                              4.12 |                   4.35 |
| Mistral-Small-24B-Instruct-2501 |          4.4  |                           4.75 |                         4.06 |                              4.29 |                   4.41 |
| Qwen2.5-72B-Instruct            |          4.54 |                           4.86 |                         4.15 |                              4.41 |                   4.53 |

### Average Performance Translations
|                                 |   Average Translation Score (Excl. Self) |   Average Translation Score (Incl. Self) |
|:--------------------------------|-----------------------------------------:|-----------------------------------------:|
| DeepSeek-V3                     |                                     4.65 |                                     4.7  |
| Meta-Llama-3.1-405B-Instruct    |                                     4.6  |                                     4.67 |
| Qwen2.5-72B-Instruct            |                                     4.49 |                                     4.5  |
| Mistral-Small-24B-Instruct-2501 |                                     4.4  |                                     4.38 |
| Meta-Llama-3.1-8B-Instruct      |                                     4.35 |                                     4.3  |

### Strictness in Evaluating Translations
|                                 |   Evaluation Strictness |
|:--------------------------------|------------------------:|
| Meta-Llama-3.1-8B-Instruct      |                    4.12 |
| Mistral-Small-24B-Instruct-2501 |                    4.47 |
| DeepSeek-V3                     |                    4.51 |
| Qwen2.5-72B-Instruct            |                    4.57 |
| Meta-Llama-3.1-405B-Instruct    |                    4.82 |




-----

# Minor stuff that isnt really working yet
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



