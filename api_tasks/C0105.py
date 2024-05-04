from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI

## PREPARING A RESPONSE
question = 'What is the main ingredient of jalapeno pizza?'

data = {'question': question}
response = requests.post(url_second, data=data)
response_parsed = json.loads(response.text)["answer"]

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": 'Jesteś weryfikatorem i sprawdzasz czy odpowiedź jest na temat. Będę podawać Ci to w takiej formie "question: pytanie", "anwser: odpowiedź". Jezeli odpowiedz jest na temat zwróć YES, a jezeli nie jest na temat zwróć NO.'},
    {"role": "user", "content": f'"question: {question}", "anwser: {response_parsed}"'}
  ]
)

chat_answer = completion.choices[0].message.content

def check_answer(chat_answer):
    if chat_answer == "YES" or chat_answer == "NO":
       return chat_answer 
    else:
        print("Error. Try again")
        exit(0)

check_answer(chat_answer)
answer = chat_answer

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": f"{answer}"})
print(response_third.text)