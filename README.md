# LLM-Eval

This repository contains the unofficial code for the paper "LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open-Domain Conversations with Large Language Models" by [Lin et al. (2023)](https://arxiv.org/abs/2305.13711).

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
python3 run_batch.py -a 0 -b 5      # Replicates the results using scores [from 0 to 5]
# - or -
python3 run_batch.py -a 0 -b 100    # Replicates the results using scores [from 0 to 100]
```

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

Additionally, the batch identifier can also be found on [OpenAI's Platform](https://platform.openai.com/batches).

