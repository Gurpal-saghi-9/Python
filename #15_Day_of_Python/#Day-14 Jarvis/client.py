
from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  # api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
