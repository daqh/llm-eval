# LLM-Eval

![Header Image](/asset/header_animation.gif)

This repository contains unofficial code for the paper "LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open-Domain Conversations with Large Language Models" by Lin et al. (2023).

This project applies the LLM-Eval framework to the PersonaChat dataset to assess response quality in a conversational context. Using GPT-4o-mini via the OpenAI API, the system generates scores (on a 0-5 or 0-100 scale) for four evaluation metrics: context, grammar, relevance, and appropriateness. The generated scores are then compared with human annotations, and the correlation is measured using Pearson, Spearman, and Kendall’s Tau coefficients.

## How to setup the environment

```bash
# Create a new environment 
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

# Install the requirements
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and fill in the necessary information.

## How to run the code

In order to produce the results of the paper, you need to run the following commands:

1. Run the experiments

```bash
python3 run_batch.py -a 0 -b 5 -m gpt-4o-mini     # Replicates the results using scores [from 0 to 5]
# - or -
python3 run_batch.py -a 0 -b 100 -m gpt-4o-mini    # Replicates the results using scores [from 0 to 100]
```

You can specify any model available on the OpenAI API. A list of models can be found [here](https://openai.com/api/pricing/).

These commands will create a batch file with the input data and send it to the OpenAI API. The output of the command will look like this:

```bash
🛢️ Loading dataset from pc_usr_data.json
📁 Stored requests in batchinput.jsonl                                

Input File Details
        📁 Name batchinput.jsonl
        🆔 ID file-[FILE_IDENTIFIER]
        💾 Bytes 812411
        📊 Status processed
Batch Details
        🆔 ID batch_[BATCH_IDENTIFIER]
        ⏰ Completion Window 24h
        🛜 Endpoint /v1/chat/completions
        📁 Input File ID file-[FILE_IDENTIFIER]
        📊 Status validating
```

In order to retrieve the results, you should copy the `batch_[BATCH_IDENTIFIER]` and run the following command:

2. Load the results

```bash
python3 load_batch.py batch_[BATCH_IDENTIFIER]
```

Note thath, the command output will present a batch progress if the batch is still processing.

Additionally, the batch identifier can also be found on [OpenAI's Platform](https://platform.openai.com/batches).

The output of the above command will look like this:

```bash
===== Pearson =====
                        content   grammar  relevance  appropriateness
avg_understandable     0.215955  0.205903   0.243477         0.219548
avg_natural            0.441733  0.452959   0.418004         0.458911
avg_maintains_context  0.484232  0.087857   0.545199         0.554493
avg_engaging           0.338908  0.094160   0.318732         0.317295
avg_uses_knowledge     0.522484  0.103329   0.550135         0.502862

===== Kendall =====
                        content   grammar  relevance  appropriateness
avg_understandable     0.214378  0.244810   0.220963         0.225096
avg_natural            0.394293  0.345629   0.364810         0.406473
avg_maintains_context  0.398185  0.057896   0.427690         0.441805
avg_engaging           0.332145  0.063244   0.292944         0.290001
avg_uses_knowledge     0.463811  0.095284   0.475252         0.445239

===== Spearman =====
                        content   grammar  relevance  appropriateness
avg_understandable     0.240211  0.255376   0.248032         0.248370
avg_natural            0.458765  0.374023   0.431535         0.465314
avg_maintains_context  0.481184  0.065730   0.515119         0.520318
avg_engaging           0.393004  0.073037   0.348444         0.342798
avg_uses_knowledge     0.536816  0.102409   0.551348         0.503047
```
