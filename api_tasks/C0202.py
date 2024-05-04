from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)
question = task_content_parsed["question"]
sentences = task_content_parsed["input"]

## PREPARING A RESPONSE
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "Jesteś weryfikatorem i zwracasz mi tylko imię w zdaniu."},
    {"role": "user", "content": question}
  ]
)

name = completion.choices[0].message.content

for sentence in sentences:
    if name in sentence:
        answer = sentence

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": f"{answer}"})
print(response_third.text)