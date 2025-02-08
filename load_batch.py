import json
from tqdm.auto import tqdm

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from time import sleep

import argparse

def load_batch(batch_id):
    client = OpenAI()
    while True:
        batch = client.batches.retrieve(batch_id)
        print("\t📈 Status", batch.request_counts.completed, "/", batch.request_counts.total, batch.status, end="\r")
        if batch.status == "completed":
            break
        sleep(10)

    output_file_id = batch.output_file_id
    output_file = client.files.content(output_file_id)

    with open("batchoutput.jsonl", "w") as f:
        f.write(output_file.text)

    from evaluation import evaluation
    df_source = evaluation()

    from transform import transform
    df_eval = transform()

    df = df_source.merge(df_eval, on='custom_id')

    print()
    print('=' * 5, 'Pearson', '=' * 5)
    print(df[['avg_understandable', 'avg_natural', 'avg_maintains_context', 'avg_engaging', 'avg_uses_knowledge', 'avg_overall', 'content', 'grammar', 'relevance', 'appropriateness']].corr('pearson').iloc[:5, 6:])
    
    print()
    print('=' * 5, 'Kendall', '=' * 5)
    print(df[['avg_understandable', 'avg_natural', 'avg_maintains_context', 'avg_engaging', 'avg_uses_knowledge', 'avg_overall', 'content', 'grammar', 'relevance', 'appropriateness']].corr('kendall').iloc[:5, 6:])
    
    print()
    print('=' * 5, 'Spearman', '=' * 5)
    print(df[['avg_understandable', 'avg_natural', 'avg_maintains_context', 'avg_engaging', 'avg_uses_knowledge', 'avg_overall', 'content', 'grammar', 'relevance', 'appropriateness']].corr('spearman').iloc[:5, 6:])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the OpenAI API')

    parser.add_argument('batch_id', type=str, help='Batch ID')

    args = parser.parse_args()
    load_batch(args.batch_id)
