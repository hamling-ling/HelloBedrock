import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name = "us-east-1")
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": "味噌汁の作り方を説明してください"
            }
        ]
    }
)
modelId = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
accept = 'application/json'
contentType = 'application/json'
response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get('body').read())
answer = response_body["content"][0]["text"]
print(answer)
