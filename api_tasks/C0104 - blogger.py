from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
blog = task_content_parsed['blog']

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": 'Jesteś pizza masterem. Napisz 4 rozdziały dotyczące pizzy Margherity. Odpowiedź zwróć w takiej formie {"answer":["tekst 1","tekst 2","tekst 3","tekst 4"]}'},
    {"role": "user", "content": f"{blog}"}
  ]
)

blog_post = completion.choices[0].message.content
blog_post = json.loads(blog_post)['answer']

answer = blog_post

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": answer})
print(response_third.text)