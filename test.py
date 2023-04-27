import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-kr1OG3zTxuHnLhRvWEusigNZ"
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.Model.list())
