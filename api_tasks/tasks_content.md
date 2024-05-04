# Task content
In the course **AI_Devs 2** I had the opportunity to do a lot of exercises with LLMs. The task system consisted of receiving the content of the task, and then preparing the solution and sending the answer as a JSON file to the corresponding endpoint. Below I present the content of the tasks for which the scripts were documented.
I mainly used the OpenAI API [https://platform.openai.com/docs/assistants/overview](https://platform.openai.com/docs/assistants/overview)

## C0101
The task was to respond by returning the 'cookie' value from the task content to anwser.

## C0104 - moderation
The task was to moderate the content of 4 sentences (0 - if the content should pass or 1 should not pass) and answer in the form of an array, e.g. [0,1,1,0].

## C0104 - blogger
The task was to have LLM generate a blog post according to an imposed text structure that specified what was to be in specific chapters.

## C0105 
TThe task was for the LLM to verify that the answer to the question returned by the task system was correct.

## C0202
The task was to send an answer to a question about a specific person based on a list with data about different people. I used LLM to extract the name from the question, and then selected a sentence from the list that contained the specific name.

## C0203
The task was to generate an embedding for the specific phrase “Hawaiian pizza.”

## C0204
The task was to generate text based on an mp3 recording using whisper [https://openai.com/index/whisper](https://openai.com/index/whisper)

## C0301
The task was to replace personal data such as first name, last name, city with placholders such as %name%, %name%, %city% and %profession% in the message sent in the task. 

## C0302
The task was to scrape a file from the page and answer a question based on it.

## C0304
The task was to use qdrant vector base and answer the question on that basis. [https://qdrant.tech](https://qdrant.tech)

## C0401
The task consisted of answering random questions about the exchange rate, selected population using NPB API, restcountries API or general knowledge. The task was to select the appropriate tool and then answer.

## C0402
The task was to classify the submitted tasks into the appropriate categories and return them as JSON.

## C0403
The task was to answer the color of the hat worn by the gnome in the submitted picture.

## C0501
The task was to generate a meme on a template that was previously created using the Renderform tool API.
[https://renderform.io/](https://renderform.io/)

## C0502
The task was to optimize the database from 30kb to 9kb while retaining all the information in the database and ensuring the ability to answer the test questions.


