import json
from utils import get_requests
from tqdm.auto import tqdm

DATASET = "pc_usr_data.json"
BATCHFILE = "batchinput.jsonl"

def store_requests(score_a, score_b):
    print("🛢️ Loading dataset from", DATASET)
    dataset = json.load(open(DATASET, "r"))
    requests = get_requests(dataset, score_a, score_b)

    # Store requests in a file according to the format required by OpenAI Batch API
    with open(BATCHFILE, "w") as f:
        for request in tqdm(requests, leave=False):
            f.write(json.dumps(request) + "\n")
    print("📁 Stored requests in", BATCHFILE)

if __name__ == "__main__":
    store_requests()
