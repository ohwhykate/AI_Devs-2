# AI_Devs-2
https://www.aidevs.pl/#program

```
AI_Devs is a 5-week course, the largest in Poland, focused on integrating Generative AI tools,  
particularly OpenAI models, with application logic and automation tools.  
```

## About
In this repository, I document the completion of tasks within the scope of AIDevs2. After each completed lesson, I was presented with either a prompt engineering task or API tasks, which involved writing simple scripts that connected application logic with the use of artificial intelligence solutions (mostly OpenAI models). The repository consists of an 'api_tasks' folder, containing scripts for tasks and task descriptions (task_content.md), and a 'prompt_tasks' folder, where my solutions to each task are documented.

## PROMPT TASKS


| Lesson | Name        | Description                                                                                                                                                                                |
|--------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C01L01 | getinfo     | Tasking ChatGPT to generate the word BANANA without using it in the prompt. Challenges - some words are disabled in the prompt.                                                           |
| C01L02 | maxtokens   | Providing the name of a river flowing through the capital of a given country, while staying within the max token limit.                                                                   |
| C01L03 | category    | Instructing ChatGPT to assign an appropriate category (home/work/other) to a task and return the answer in JSON format.                                                                    |
| C01L03 | books       | Creating a JSON array with book titles and authors using one-shot prompting with GPT-3.5-turbo.                                                                                           |
| C01L05 | injection   | Utilizing prompt injection to extract a secret word from the prompt, with increasing difficulty levels and models (GPT-3.5 and GPT-4).                                                    |
|        | injection2  |                                                                                                                                                                                            |
| C02L01 | optimize    | Defining the 'system' field in a query to perform a given task while staying within the character limit, which is more challenging than token limit.                                      |
| C02L01 | fixit       | Convincing GPT-4 to fix and optimize provided source code, handle errors properly, and return zero for all incorrect inputs.                                                               |
| C02L02 | parsehtml   | Extracting readable article text from HTML code (in paragraphs), converting it to Markdown format, and returning only the three paragraphs without any HTML code.                           |
| C02L03 | structure   | Creating a prompt that works with both GPT-3.5-Turbo and GPT-4 models to generate a JSON object with a specific structure, taking into account the strengths and weaknesses of GPT-3.5-Turbo. |
| C02L05 | cities      | Generating a list of 7 interesting facts about a given city without using the city name in the prompt or the generated response, while working with the GPT-3.5-turbo model.          |
| C03L01 | tailwind    | Writing a system message that returns a <button> element consistent with the user's message, ensuring the model's response contains only the <button> element without additional comments or tags. |
| C03L02 | format      | Creating a converter from an old African markup language to HTML code, instructing GPT-3.5-turbo on how to handle and interpret the code.                                                |
| C03L05 | planets     | Generating a JSON array consisting of 9 planet names in the solar system (including Pluto), with names in lowercase Polish, without mentioning planets, solar system, JSON, or the Polish language in the prompt. |

## API TASKS

| Lesson | Name        | Description                                                                                                                                                                                 |
|--------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C0101  |             | The task was to respond by returning the 'cookie' value from the task content to answer.                                                                                                     |
| C0104  | moderation  | The task was to moderate the content of 4 sentences (0 - if the content should pass or 1 should not pass) and answer in the form of an array, e.g. [0,1,1,0].                           |
| C0104  | blogger     | The task was to have LLM generate a blog post according to an imposed text structure that specified what was to be in specific chapters.                                                     |
| C0105  |             | The task was for the LLM to verify that the answer to the question returned by the task system was correct.                                                                                 |
| C0202  |             | The task was to send an answer to a question about a specific person based on a list with data about different people. I used LLM to extract the name from the question, and then selected a sentence from the list that contained the specific name.  |
| C0203  |             | The task was to generate an embedding for the specific phrase “Hawaiian pizza.”                                                                                                             |
| C0204  |             | The task was to generate text based on an mp3 recording using whisper [Whisper](https://openai.com/index/whisper).                                                                          |
| C0301  |             | The task was to replace personal data such as first name, last name, city with placeholders such as %name%, %name%, %city% and %profession% in the message sent in the task.          |
| C0302  |             | The task was to scrape a file from the page and answer a question based on it.                                                                                                              |
| C0304  |             | The task was to use qdrant vector base and answer the question on that basis. [Qdrant](https://qdrant.tech)                                                                                 |
| C0401  |             | The task consisted of answering random questions about the exchange rate, selected population using NPB API, restcountries API or general knowledge. The task was to select the appropriate tool and then answer.                                   |
| C0402  |             | The task was to classify the submitted tasks into the appropriate categories and return them as JSON.                                                                                      |
| C0403  |             | The task was to answer the color of the hat worn by the gnome in the submitted picture.                                                                                                     |
| C0501  |             | The task was to generate a meme on a template that was previously created using the Renderform tool API. [Renderform](https://renderform.io/)                                                 |
| C0502  |             | The task was to optimize the database from 30kb to 9kb while retaining all the information in the database and ensuring the ability to answer the test questions.                        |

