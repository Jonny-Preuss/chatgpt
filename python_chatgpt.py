import requests
import os
#import openai
import argparse

## specifying the prompt
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
#parser.add_argument("file_name", help="Name of the Python script file we are creating")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

## providing meta-data for POST request
request_headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + api_key ## or with $ sign?
                    }


## providing prompt specifications
request_data = {"model": "text-ada-001",
                "prompt": f"Write a Python script to {args.prompt}. Provide only code, no text.", ## what if I want commented code?
                "max_tokens": 100,
                "temperature": 0.5,
                #"top_p": 1,
                #"n": 1,
                #"stream": false,
                #"logprobs": null,
                #"stop": "\n"
                }

response = requests.post(api_endpoint, headers=request_headers, json=request_data, timeout=5)

if response.status_code==200:
    response_text = response.json()["choices"][0]["text"]
    with open("chatgpt_output.py", "w") as file:
    #with open("args.file_name", "w") as file:
        file.write(response_text)
else: print(f"Request failed with status code: {str(response.status_code)}")
