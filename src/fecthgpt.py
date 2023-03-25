import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
model_engine = "gpt-3.5-turbo"

max_tokens = 256

def getGPTResponse(role, text, data):
    prompt = f"{data['name']} is a {data['age']} year old who lives in {data['location']}. He is a {data['occupation']} and likes to do {data['hobbies']}Give me some trends about climate change where he lives and a list of things (specific to where he lives) he can do to help the climate where he lives "
    message = [{"role" : role, "content" : text}]

    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=message,
        max_tokens=max_tokens,
        temperature=.4,
    )

    return completion.choices[0]['message']["content"]