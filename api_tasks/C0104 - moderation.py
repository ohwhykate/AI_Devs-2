from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
client = OpenAI()

input = task_content_parsed['input']

moderation = client.moderations.create(input=input)

results = [
    1 if result.flagged else 0 
    for result in moderation.results
]

answer = results

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": answer})
print(response_third.text)