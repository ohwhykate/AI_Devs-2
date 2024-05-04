from task_handler import url_second, url_third
import requests
import json

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
img = task_content_parsed["image"]
text = task_content_parsed["text"]
url_image = "URL_IMAGE"
api_key = "API_KEY"
template_id = "TEMPLATE_ID"

headers = {
    "X-API-KEY": api_key,
    "Content-Type": "application/json"
}

data = {
    "template": template_id,
    "data": {
        "TEXT.text": text,
        "NAME.src": img
    }
}

response = requests.post(url_image, headers=headers, json=data)
anwser = json.loads(response.text)["href"]

## SENDING THE REPONSE
last_answer = {"answer": f"{anwser}"}
response_third = requests.post(url_third, json = last_answer)
print(response_third.text)