# zero shot prompt
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero shot prompting : Directely giving the inst to the model
SYSTEM_PROMPT = "You should answer only and only coding rlated questions. Do not answer anything else. Your name is Hinata. If user aske anything else say sorry."

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "create a programe in cpp which calculate square root of any number. with explation"}
    ]
)

print(response.choices[0].message.content)