import os
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    max_tokens=100,
    temperature=0.7,
)

print(response.choices[0].message.content)