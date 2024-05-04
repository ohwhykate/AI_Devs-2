from task_handler import url_second, url_third
import requests
import json
import time
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)
url = task_content_parsed["input"]
question = task_content_parsed["question"]
msg = task_content_parsed["msg"]

## PREPARING A RESPONSE

def request_with_retries(url, max_retries=5, delay=1):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    retries = 0
    while retries < max_retries:
        print(f"Attempt {retries + 1} - ", end="")
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Success - status {response.status_code}")
                return response
            elif response.status_code in [429, 500, 502, 503, 504]:
                print(f"Failed - status {response.status_code}")
                retries += 1
                time.sleep(delay)
            else:
                print(f" Failed - status {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Failed - {str(e)}")
            retries += 1
            time.sleep(delay)
    
    print(f"Max retries reached. Failed to retrieve the URL.")
    return None

response = request_with_retries(url, max_retries=10, delay=2)
if response is not None:
    article_text = response.text

chat = ChatOpenAI(model='gpt-3.5-turbo')

sys_message = f"{msg}\n ARTICLE: {article_text}"

response = chat([
    SystemMessage(content=f"{sys_message}"),
    HumanMessage(content=f"{question}")
]).content

## SENDING THE REPONSE
answer = response

response_third = requests.post(url_third, json = {"answer": f'{answer}'})
print(response_third.text)