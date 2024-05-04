from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI
import pandas as pd

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
question = task_content_parsed["question"]
msg = task_content_parsed["msg"]
example_to_do = task_content_parsed["example for ToDo"]
example_calendar = task_content_parsed["example for Calendar"]
hint = task_content_parsed["hint"]

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  # response_format= {"type": "json_object"},
  messages=[
    {"role": "system", "content": f"{msg} Example for ToDo: {example_to_do} Example for Calendar: {example_calendar} and hint for the calendar: {hint} Dzisiaj jest 2024-05-04 "},
    {"role": "user", "content": f"{question}" }
  ]
)

json_answer = completion.choices[0].message.content
json_answer = json.loads(json_answer)

print(json_answer)

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": json_answer})
print(response_third.text)