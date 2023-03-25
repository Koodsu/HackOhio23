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




generate_chat_completion("What is Obamas last name")