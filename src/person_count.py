import boto3
import json
import base64

#FILENAME="crowd.jpg"
#FILENAME="single.jpg"
#FILENAME="stroller.jpg"
FILENAME="wheel_chair.jpg"

with open(f"./jpg/{FILENAME}", "rb") as f:
    image = f.read()
    b64 = base64.b64encode(image).decode("utf-8")

bedrock = boto3.client('bedrock-runtime', region_name = "us-east-1")
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": b64
                        }
                    },
                    {
                        "type": "text",
                        "text": "I want you to count number of people, wheel charis and strollers. How many are they? Give me a set of numbers (x,y,z) where x is a number of person, y is a number of wheel chairs and z is a number of strollers"
                    }
                ]
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
