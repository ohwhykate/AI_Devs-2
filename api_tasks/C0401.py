from task_handler import url_second, url_third
import requests
import json
from openai import OpenAI
import pandas as pd

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)
question = task_content_parsed["question"]
msg = task_content_parsed["msg"]

## PREPARING A RESPONSE
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  # response_format= {"type": "json_object"},
  messages=[
    {"role": "system", "content": f"{msg}.You have only 3 option (1 - exchange rate, 2 - population, 3 - general knowlegde.). Return anwser in special format\n ##EXAMPLES:\n If question will be about exchange rate, return code exchange in special format (for example: 1 THB; 1 USD), if question will be about population, return country name (for example: 2 Moldova; 2 United States. If it will question from general knowledge anwser it(for example: 3 your anwser.) "},
    {"role": "user", "content": question}
  ]
)

json_answer = completion.choices[0].message.content
json_answer_array = json_answer.split(maxsplit=1)

API_1 = "http://api.nbp.pl/api/exchangerates/tables/A"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
response_api_1 = requests.get(API_1, headers=headers)
content_response_1 = json.loads(response_api_1.text)
df_api_1 = pd.DataFrame(content_response_1[0]['rates'])

API_2 = "https://restcountries.com/v3.1/all?fields=population,name"
response_api_2 = requests.get(API_2, headers=headers)
content_response_2 = json.loads(response_api_2.text)
countries = [country['name']['common'] for country in content_response_2]
populations = [country['population'] for country in content_response_2]
df_api_2 = pd.DataFrame({'Country': countries, 'Population': populations})


if json_answer_array[0] == '1':
    anwser = df_api_1.loc[df_api_1["code"] == json_answer_array[1], 'mid'].iloc[0]
elif json_answer_array[0] == '2':
    anwser = df_api_2.loc[df_api_2['Country'] == json_answer_array[1], 'Population'].iloc[0]
elif json_answer_array[0] == '3':
    anwser = json_answer_array[1]
else:
    print("Error")

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": f"{anwser}"})
print(response_third.text)