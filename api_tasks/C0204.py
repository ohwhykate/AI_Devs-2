from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

def download_mp3_from_url(url, save_path):
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)

## PREPARING A RESPONSE
url = task_content_parsed['msg'].split("file: ")[1]
save_path = '~/AIDEVS2/api_tasks/plik.mp3'

download_mp3_from_url(url, save_path)
client = OpenAI()

audio_file= open(save_path, "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
answer = transcription.text

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": answer})
print(response_third.text)