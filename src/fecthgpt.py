import openai

openai.api_key = "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"
model_engine = "gpt-3.5-turbo"
prompt = "Write an essay about climate change"

max_tokens = 256

messages = [{"role": "system", "content": "Write an essay about climate change"}]

completion = openai.ChatCompletion.create(
    model=model_engine,
    messages = messages

)

print(completion.choices[0]['message']["content"])
