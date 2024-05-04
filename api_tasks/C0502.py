from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
msg = task_content_parsed["msg"]
database_url = task_content_parsed["database"]

database_scheme = requests.get(database_url)
database_scheme_json = database_scheme.text

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_format= {"type": "json_object"},
  messages=[
    {"role": "system", "content": f"{msg} in 9kb or less memory. Anwser it in JSON."},
    {"role": "user", "content": f"{database_scheme_json}" }
  ]
)

answer = completion.choices[0].message.content

last_answer = {"answer": answer}
response_third = requests.post(url_third, json = last_answer)
print(response_third.text)
