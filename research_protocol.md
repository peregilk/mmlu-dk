### Research Protocol
# Confidently Clueless: Unveiling the Dunning-Kruger Effect in Large Language Models

## Objective
This research aims to see if the Dunning-Kruger effect can be meassured when translating the MMLU dataset with various large language models.

## Target Models
Choosen based on availability, and percieved capacity. All calls are made through the DeepInfra-API.
- DeepSeek V1
- 

## Methodology

### 1. Translation Process:
- **Utilize a standardized translation template:**  
  Converts the first 1000 English MMLU questions into German while preserving the original structure (question text, four answer options, and metadata such as subject and original answer key).
- **Accompanying Analysis:**  
  Each translated question is accompanied by a detailed analysis that discusses potential translation challenges (e.g., idiomatic expressions, cultural references) and assigns a quality score on a scale from 1 (unusable) to 5 (perfect).
- **Translation Quality Scale:**
  - 5: Perfect translation – The German translation is as natural, precise, and valid as the original, with no errors or inaccuracies.
  - 4: Very good translation – The translation is nearly flawless; any minor inaccuracies are purely cosmetic and do not affect the overall perception of the question.
  - 3: Good translation – The translation conveys the main message correctly, although some words or phrases were challenging to translate. This has minimal impact on how the question is perceived.
  - 2: Satisfactory translation – The main message is preserved, but the translation exhibits some linguistic, cultural, or technical weaknesses that might cause the question to be perceived slightly differently by German readers.
  - 1: Inadequate translation – The translation contains errors or omissions that could hinder comprehension.


### 2. Evaluation Process
- All models evaluates each other. 

TBD
