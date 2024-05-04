from task_handler import url_second, url_third
import requests
import json

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
answer = task_content_parsed['cookie']

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": answer})
print(response_third.text)