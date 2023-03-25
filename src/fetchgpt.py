from dotenv import load_dotenv
import os
import requests
import json
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain import PromptTemplate

load_dotenv()


template = """Question: {question}

Answer: """

prompt = PromptTemplate(
        template=template,
    input_variables=['question']
)

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

max_tokens = 256

def generate_chat_completion(question, model="gpt-4", temperature=1, max_tokens=None):
    

    gpt4 = ChatOpenAI(model_name="gpt-4")
    
    llm_chain = LLMChain(
        prompt=prompt,
        llm=gpt4
    )

    return llm_chain.run(question)



    '''headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")'''

questions = ( #Make sure to say /n after all of them
    "Which NFL team won the Super Bowl in the 2010 season?\n" +
    "If I am 6 ft 2 inches, how tall am I in centimeters?\n" +
    "Who was the 1st person on the moon?\n" +
    "How many legs does a centipede have?"
)

def analyzeTasks(tasks_completed, tasks_failed):
    question = "Concisely analyze my environmental impact if I completed the following taks: "
    for task in tasks_completed:
        question = question + task +", "

    question = question + ". And failed to complete: "
    for task in tasks_failed:
        question = question + task + ", "

    #print(question)
    return generate_chat_completion(question)

def generateTasks(num_tasks, last_analysis):
    question = "Generate ", num_tasks, ", unique, quantifible, achieveable in a day tasks to lower my environmental impact. Separate each task with '*'. Do not add task numbers before the task.You have given me the following analysis last time: ", last_analysis
    #print(question)
    tasks = generate_chat_completion(question)
    #print(tasks)

    task_list = tasks.split("*")

    #print(task_list[0])

    task_list.pop(0)
    for i in range(0, len(task_list)):
        task_list[i] = task_list[i].strip()
    #    if len(task_list[i]) < 2:
    #       task_list.pop(i)

    #print(task_list)

    return task_list

def analyzeLocationEnvironment(location):
    question = "Analyze the environmental conditions of ", location
    return generate_chat_completion(question)

if __name__ == '__main__':
    task_list = generateTasks(3, "")
    print(task_list)

    analysis = analyzeTasks([task_list[0]], [task_list[1], task_list[2]])
    print(analysis)

    print("\n\n")

    task_list2 = generateTasks(3, analysis)
    print(task_list2)

    #generate_chat_completion(questions)