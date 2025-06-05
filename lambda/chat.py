import json
import os
import urllib.request

def lambda_handler(event, context):
    question = event.get("question")
    if not question:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing "question" in input'})
        }

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Missing OpenAI API key in environment'})
        }

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 150
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read()
            res_data = json.loads(res_body)
            answer = res_data['choices'][0]['message']['content']
            print(f"Q: {question}")
            print(f"A: {answer}")
            return {
                'statusCode': 200,
                'body': json.dumps({'answer': answer})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
