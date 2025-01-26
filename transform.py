import pandas as pd
import json

def transform():
    with open("batchoutput.jsonl", "r") as f:
        evaluations = []
        for line in f:
            data = json.loads(line)
            custom_id = data['custom_id']
            content = json.loads(data['response']['body']['choices'][0]['message']['content'])
            content['custom_id'] = int(custom_id)
            evaluations.append(content)
        df = pd.DataFrame(evaluations, dtype=float)
    return df

if __name__ == '__main__':
    transform()
