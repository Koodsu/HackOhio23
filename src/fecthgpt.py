import openai
from dotenv import load_env
import os
load_env()

openai.api_key = os.getenv('OPENAI_API_KEY')
model_engine = "gpt-3.5-turbo"
prompt = "Write an essay about climate change"

max_tokens = 256

messages = [{"role": "system", "content": "Write an essay about climate change"}]

completion = openai.ChatCompletion.create(
    model=model_engine,
    messages = messages

)

print(completion.choices[0]['message']["content"])
