from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system","content": "You are expret in physics and only answer the physics related answer"},
        {"role":"user","content":"Hey, can you tell me a 3rd law of newton's"}
    ]
)

print(response.choices[0].message.content)