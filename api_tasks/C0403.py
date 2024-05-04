from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
msg = task_content_parsed["msg"]
hint = task_content_parsed["hint"]
url_photo = task_content_parsed["url"]

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": f"{msg} {hint}"},
        {
          "type": "image_url",
          "image_url": {
            "url": url_photo,
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

anwser = response.choices[0].message.content

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": f"{anwser}"})
print(response_third.text)