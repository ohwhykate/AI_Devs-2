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

