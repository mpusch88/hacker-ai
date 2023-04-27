import os
import sys
import time
import openai
import keyboard
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-kr1OG3zTxuHnLhRvWEusigNZ"
openai.api_key = os.getenv("OPENAI_API_KEY")


def loading_message(num_dots):
    for i in range(num_dots):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\r")
    sys.stdout.flush()


history = []
firstRun = True
args = sys.argv
inputString = ""

for arg in args:
    if firstRun == True:
        firstRun = False
        continue

    inputString += arg + " "

while len(history) < 5:
    if keyboard.is_pressed("esc"):
        break

    if len(history) == 0:
        hacker_preamble = "Please respond to all following user messages as if you were an edgy hacker from an 80s movie. give code only responses when asked for code. Ensure answers are less than 200 tokens. \n\n"
        if inputString == "":
            user_input = hacker_preamble + "good day hacker..."
        else:
            user_input = hacker_preamble + inputString
    else:
        user_input = input("")

        if user_input == "q":
            break

        user_input = "message: " + user_input

    messages = []

    for input_text, completion_text in history:
        messages.append({"role": "user", "content": input_text})
        messages.append({"role": "assistant", "content": completion_text})

    messages.append({"role": "user", "content": user_input})

    loading_message(3)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=0.7,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        top_p=1,
    )

    sys.stdout.write("\r" + " " * (len("connecting...") + 3) + "\r")
    sys.stdout.flush()

    completion_text = completion.choices[0].message.content

    print(f"{completion_text}")

    history.append((user_input, completion_text))

print("dropping connection...")
