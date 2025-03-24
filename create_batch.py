from openai import OpenAI
from utils import get_client

def create_batch(batch_input_file):
    client = get_client()

    batch = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )
    return batch
