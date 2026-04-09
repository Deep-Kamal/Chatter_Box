# chain of Thought Prompting
from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You are an expert AI Assistant in resolving user queries in chain of thought 
    You work on START, PLAN and OUTPUT steps.
    You need to PLAN what need to done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    
    Rules:
    -Strictly Follow the given JSON format
    -Only run one step at a time.
    -The sequence of step is START ( where user give an input ), PLAN (That can be     multiple times) and finally OUTPUT (which is going to the displayed to the user).
    
    Output JSON format:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}
    
    Example:
    START: Hey, can you slove 2+3*5/10
    PLAN: {"step": "PLAN": "content": "Seem like user is instersted in maths problem"}
    PLAN: {"step": "PLAN": "content": " looking at the problem, we should slove this using BODMAS method "}
    PLAN: {"step": "PLAN": "content": " first be multiply 3*5 which is 15 "}
    PLAN: {"step": "PLAN": "content": " after that be divided the 15 by 10 get 1.5 "}
    PLAN: {"step": "PLAN": "content": " Now add 1.5 to 2 then be get finial result 3.5 "}
    
    OUTPUT: {"step": "OUTPUT": "content": " 3.5 "}
    
"""

print("\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("WRITE:-")
message_history.append({"role":"user","content":user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        response_format={"type": "json_object"},
        messages=message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    
    parsed_result = json.loads(raw_result)
    
    
    if parsed_result.get("step") == "START":
        print("THINKING:-", parsed_result.get("content"))
        continue
    
    elif parsed_result.get("step") == "PLAN":
        print("PROCSSING:-", parsed_result.get("content"))
        continue
    
    elif parsed_result.get("step") == "OUTPUT":
        print("RESULT:-", parsed_result.get("content"))
        break

print("\n")