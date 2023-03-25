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

multi_template = """Answer the following questions one at a time.

Questions:
{questions}

Answers:
"""

prompt = PromptTemplate(
        template=template,
    input_variables=['question']
)

long_prompt = PromptTemplate(template=multi_template, input_variables=["questions"])

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

max_tokens = 256

def generate_chat_completion(question, model="gpt-4", temperature=1, max_tokens=None):
    

    gpt4 = ChatOpenAI(model_name="gpt-4")
    
    llm_chain = LLMChain(
        prompt=long_prompt,
        llm=gpt4
    )

    print(llm_chain.run(question))



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


generate_chat_completion(questions)