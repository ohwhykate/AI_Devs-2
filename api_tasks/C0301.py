from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)
message = task_content_parsed["msg"]

## PREPARING A RESPONSE
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  # response_format= {"type": "json_object"},
  messages=[
    {"role": "system", "content": 'I will give you the message. Ecrypt the message and replace name, surname, city and profession with placeholders. Placeholders list {%imie%, %nazwisko%, %zawod% and %miasto%}. EXAMPLE: I am %imie% %nazwisko%. I am from %miasto%. I am working as %zawod%.'},
    {"role": "user", "content": message}
  ]
)

answer =  completion.choices[0].message.content

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": f'{answer}'})
print(response_third.text)