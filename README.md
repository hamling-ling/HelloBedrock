# Hello Bedrock

## Ubuntu 24.04 Setup

```
sudo apt install python3.12-venv
python3 -m venv py3
source ~/py3/bin/activate
```

## AWS 側設定

* Amazon Bedrock のはじめ方
    * https://qiita.com/icoxfog417/items/869e2093e672b2b8a139

* Check for available models
    ```
    aws bedrock list-foundation-models --region us-east-1
    ```

## How to Run


### Single shot

Command
```
cd src
python3 person_count.py
```
Output:
```
Based on the image provided, I can give you the following count:

(2, 1, 0)

This represents:
x = 2 (two people are visible in the image)
y = 1 (one wheelchair is present)
z = 0 (no strollers are visible in this image)

The image shows two individuals at what appears to be an entrance or doorway of a building. One person is standing, while the other is seated in a wheelchair. There are no strollers present in this scene.
```

### All

Command
```
cd src
python3 person_count_all.py 
```

Output
```
answer / truth : (4, 0, 0) / (4, 0, 0)
answer / truth : (2, 0, 0) / (2, 0, 0)
answer / truth : (2, 0, 2) / (2, 0, 2)
answer / truth : (2, 1, 0) / (2, 1, 0)
```

## Reference

* Amazon Bedrock のはじめ方
    * https://qiita.com/icoxfog417/items/869e2093e672b2b8a139
* Python ( Boto3 ) からBedrockのClaude3を実行する
    * https://qiita.com/cyberBOSE/items/0e41fb7bcee6b7965d09

