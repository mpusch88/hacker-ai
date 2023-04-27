import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-kr1OG3zTxuHnLhRvWEusigNZ"
openai.api_key = os.getenv("OPENAI_API_KEY")

history = []
firstRun = True

while len(history) < 5:
    user_input = input("Your input: ")

    messages = [] # cap 
    for input_text, completion_text in history:
        messages.append({"role": "user", "content": input_text})
        messages.append({"role": "hacker", "content": completion_text})

    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    completion_text = completion.choices[0].message.content
    print(completion_text)

    history.append((user_input, completion_text))

    user_input = input("Would you like to continue the conversation? (Y/N) ")
    if user_input.upper() == "N":
        break
    elif user_input.upper() != "Y":
        print("Invalid input. Please enter 'Y' or 'N'.")
        break
    
print("Oh shit, the fuzz are here! Dropping connection")