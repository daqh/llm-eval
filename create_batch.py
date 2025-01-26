from openai import OpenAI

def create_batch(batch_input_file):
    client = OpenAI()

    batch = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )
    return batch
