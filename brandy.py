import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "list 5 items that start with letter A"}],
    temperature=0.8,
    max_tokens=256,
)

print("Created response ", response)
