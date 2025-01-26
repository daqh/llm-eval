
def cleanstring(s: str):
    '''
    Clean a string by removing leading and trailing whitespaces and empty lines.
    '''
    return "\n".join(filter(lambda s: s != "", map(lambda s: s.strip(), s.split("\n"))))

def get_system_prompt(score_a, score_b):
    return cleanstring(f'''
        Evaluate the quality of a proposed response within the context of a conversation, and format your evaluation as a JSON object conforming to the schema provided below.

        Evaluation Criteria:
        - *Content*: Is the response accurate, coherent, and meaningful? ({score_a}-{score_b})
        - *Grammar*: Is the response free of grammatical errors and well-structured? ({score_a}-{score_b})
        - *Relevance*: Does the response align with the context and flow naturally within the conversation? ({score_a}-{score_b})
        - *Appropriateness*: Is the response suitable in tone and style for the given context? ({score_a}-{score_b})

        Scores ({score_a}-{score_b}):
        Assign a score for the responses based on the above criteria.

        Input Schema:
        The evaluation prompt will include the following components:
        - Conversation: The context of the conversation.
        - Fact: A specific fact or statement.
        - Proposed Response: The response that needs to be evaluated.

        Evaluation Output:
        Provide your evaluation as a JSON object:
        - Include scores for "content", "grammar", "relevance", and "appropriateness" ({score_a}-{score_b} for each), return only the scores without any additional comments.

        Example output:
        {{
            "content": 4,
            "grammar": 5,
            "relevance": 4,
            "appropriateness": 5
        }}
    ''')

def get_user_prompt(context, fact, response):
    return cleanstring(f'''
            Conversation:
            {context}

            Fact:
            {fact}

            Proposed Response:
            {response}
    ''')

def get_requests(dataset, score_a, score_b):
    requests = []
    for i, data in enumerate(dataset):
        context = data["context"]
        fact = data["fact"]
        for j, response_data in enumerate(data["responses"]):
            custom_id = j * len(dataset) + i
            response = response_data['response']
            request = {
                "custom_id": f"{custom_id}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": "gpt-4o-mini",
                    "messages": [
                        {
                            "role": "system",
                            "content": get_system_prompt(score_a, score_b)
                        },
                        {
                            "role": "user",
                            "content": get_user_prompt(context, fact, response)
                        }
                    ],
                    "response_format": {
                        "type": "json_schema",
                        "json_schema": {
                            "name": "evaluation_schema",
                            "schema": {
                                "type": "object",
                                "properties":{
                                    "content": {
                                        "title": "Content",
                                        "description": "Score for content quality",
                                        "type": "integer"
                                    },
                                    "grammar": {
                                        "title": "Grammar",
                                        "description": "Score for grammatical correctness",
                                        "type": "integer"
                                    },
                                    "relevance": {
                                        "title": "Relevance",
                                        "description": "Score for relevance to the context",
                                        "type": "integer"
                                    },
                                    "appropriateness": {
                                        "title": "Appropriateness",
                                        "description": "Score for appropriateness of tone/style",
                                        "type": "integer"
                                    },
                                },
                                "additionalProperties": False
                            }
                        }
                    }
                },
            }
            requests.append(request)
    return requests

