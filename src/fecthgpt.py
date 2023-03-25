import openai
from dotenv import load_env
import os
load_env()

openai.api_key = os.getenv('OPENAI_API_KEY')
model_engine = "gpt-3.5-turbo"
prompt = "Write an essay about climate change"

max_tokens = 256

def getGPTResponse(role, text):
    message = [{"role" : role, "content" : text}]



    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages = message
    )

    return completion.choices[0]['message']["content"]


print(getGPTResponse("system", "what is a cpu"))



