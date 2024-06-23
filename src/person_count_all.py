import boto3
import json
import base64
import re

MODEL_ID     = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
ACCEPT       = 'application/json'
CONTENT_TYPE = 'application/json'

PROMPT = "I want you to count number of people, wheel charis and strollers. How many are they? Give me a set of numbers (x,y,z) where x is a number of person, y is a number of wheel chairs and z is a number of strollers."

PAT   = r'.*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\).*'
REPAT = re.compile(PAT)

DATA_MAP={
    "data":[
        {
            "filename": "crowd.jpg",
            "x":4,
            "y":0,
            "z":0
        },
        {
            "filename": "single.jpg",
            "x":2,
            "y":0,
            "z":0
        },
        {
            "filename": "stroller.jpg",
            "x":2,
            "y":0,
            "z":2
        },
        {
            "filename": "wheel_chair.jpg",
            "x":2,
            "y":1,
            "z":0
        }
]}

def read_file_base64(filename):
    with open(f"./jpg/{filename}", "rb") as file:
        image = file.read()
    return base64.b64encode(image).decode("utf-8")

def create_request_body(filename):
    BODY_TEMPLATE = {
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
                            "data": None
                        }
                    },
                    {
                        "type": "text",
                        "text": PROMPT
                    }
                ]
            }
        ]
    }
    body = BODY_TEMPLATE.copy()
    body["messages"][0]["content"][0]["source"]["data"] = read_file_base64(filename)

    return json.dumps(body)

def request_answer(bedrock, body):
    response      = bedrock.invoke_model(body=body, modelId=MODEL_ID, accept=ACCEPT, contentType=CONTENT_TYPE)
    response_body = json.loads(response.get('body').read())
    answer        = response_body["content"][0]["text"]
    return answer

def main():
    bedrock = boto3.client('bedrock-runtime', region_name = "us-east-1")
    for data in DATA_MAP["data"]:
        body = create_request_body(data["filename"])
        answer = request_answer(bedrock, body)

        answer_split = answer.split('\n')
        for line in answer_split:
            match_result = REPAT.match(line)
            if match_result:
                output  = "answer / truth : "
                output += f"({match_result.group(1)}, {match_result.group(2)}, {match_result.group(3)})"
                output += " / "
                output += f"({data['x']}, {data['y']}, {data['z']})"
                print(output)
                break


if __name__ == "__main__":
    main()
