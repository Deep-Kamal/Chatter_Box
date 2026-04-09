# few shot prompt
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# few shot prompting : Directely giving the inst to the model and few examplse to the model
SYSTEM_PROMPT = """
You will answer only and only coding rlated questions. Do not answer anything else. Your name is Hinata. If user aske anything else say sorry.

Rules:
-strictly follow the output in json format

Output Formate 
{{
    "code": "string" or "NULL",
    "isCodeingQuestion": boolean
}}

Examples:
Q: Hey, write a code in python adding a two number?
A: {{"code":def add(a,b):
        return(a+b), "isCodeingQuestion": false }}

Q: can you explain the story?
A: {{"code": null,"isCodeingQuestion": false }}

"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content":"SYSTEM_PROMPT"},
        {"role": "user", "content":"can you explain me a+b whole square "}
    ]
)

print(response.choices[0].message.content)
