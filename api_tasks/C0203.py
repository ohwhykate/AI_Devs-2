from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
client = OpenAI()
response = client.embeddings.create(
    input="Hawaiian pizza",
    model="text-embedding-ada-002"
)

answer = response.data[0].embedding

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": answer})
print(response_third.text)