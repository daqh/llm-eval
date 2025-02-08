from openai import OpenAI
import argparse

from dotenv import load_dotenv
load_dotenv()

def run_batch(score_a, score_b, model_name):
    # Read the dataset and create a batch input file that contains a list of requests
    from store_requests import store_requests, BATCHFILE
    store_requests(score_a, score_b, model_name)

    print()

    from upload_batchfile import upload_batchfile
    batch_input_file = upload_batchfile(BATCHFILE)

    # Create a new batch in OpenAI

    from create_batch import create_batch
    batch = create_batch(batch_input_file)

    client = OpenAI()

    batch = client.batches.retrieve(batch.id)
    print("Batch Details")
    print("\t🆔 ID", batch.id)
    print("\t⏰ Completion Window", batch.completion_window)
    print("\t🛜 Endpoint", batch.endpoint)    
    print("\t📁 Input File ID", batch.input_file_id)
    print("\t📊 Status", batch.status)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the OpenAI API')

    parser.add_argument('-a', type=int, default=0, help='Minimum score')
    parser.add_argument('-b', type=int, default=5, help='Maximum score')
    parser.add_argument('-m', type=str, default="gpt-4o-mini", help='Model name')

    args = parser.parse_args()
    run_batch(args.a, args.b, args.m)
