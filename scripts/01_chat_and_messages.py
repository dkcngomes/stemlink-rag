import os
import sys
import requests

from langchain_openai import ChatOpenAI
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env")

API_KEY = os.getenv("OPENAI_API_KEY")
QUESTION = "Name the two paddy cultivation seasons in Sri Lanka."

chat_model = ChatOpenAI(
    model_name="gpt-5.6-luna",
    openai_api_key=API_KEY,
    max_tokens=100,
    temperature=0.7,
    request_timeout=60,
)

response = chat_model.invoke([{"role": "user", "content": QUESTION}])

print("-" * 40)
print(response.content)
print("-" * 40)