import json
import pandas as pd
from store_requests import DATASET

def evaluation():
    dataset = json.load(open(DATASET, "r"))
    
    processed_data = []
    for i, data in enumerate(dataset):
        context = data['context']
        fact = data['fact']
        annotators = data['annotators']
        for j, response_data in enumerate(data['responses']):
            custom_id = j * len(dataset) + i
            response = response_data['response']
            model = response_data['model']
            understandable = response_data['Understandable']
            natural = response_data['Natural']
            maintains_context = response_data['Maintains Context']
            engaging = response_data['Engaging']
            uses_knowledge = response_data['Uses Knowledge']
            overall = response_data['Overall']
            processed_data.append({
                'custom_id': custom_id,
                'context': context,
                'fact': fact,
                'response': response,
                'model': model,
                'annotators': annotators,
                'understandable': understandable,
                'natural': natural,
                'maintains_context': maintains_context,
                'engaging': engaging,
                'uses_knowledge': uses_knowledge,
                'overall': overall
            })

    df = pd.DataFrame(processed_data)

    df['avg_understandable'] = df['understandable'].apply(lambda x: sum(x)/len(x)).to_numpy()
    df['avg_natural'] = df['natural'].apply(lambda x: sum(x)/len(x))
    df['avg_maintains_context'] = df['maintains_context'].apply(lambda x: sum(x)/len(x))
    df['avg_engaging'] = df['engaging'].apply(lambda x: sum(x)/len(x))
    df['avg_uses_knowledge'] = df['uses_knowledge'].apply(lambda x: sum(x)/len(x))
    df['avg_overall'] = df['overall'].apply(lambda x: sum(x)/len(x))
    return df

if __name__ == '__main__':
    evaluation()
