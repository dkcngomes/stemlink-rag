# Developer : @dkcngomes
import os
import sys
import requests
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env")

QUESTION = "Name the two paddy cultivation seasons in Sri Lanka."
API_KEY = os.getenv("OPENAI_API_KEY")

#========== WITH OPEN AI SDK ============== 

#from openai import OpenAI
#client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# response = client.chat.completions.create(
#     model="gpt-5.6-luna",
#     messages=[
#         {"role": "user", "content": QUESTION},
#     ],
#     max_completion_tokens=100,
# )

# print("====================================")
# print(response.choices[0].message.content)
# print("====================================")

#======== With requests ================

# def main():
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         print("Error: OPENAI_API_KEY is not set. Add it to .env or the environment.", file=sys.stderr)
#         return 1

#     try:
#         response = requests.post(
#             "https://api.openai.com/v1/chat/completions",
#             headers={
#                 "Authorization": f"Bearer {api_key}",
#                 "Content-Type": "application/json",
#             },
#             json={
#                 "model": "gpt-5.6-luna",
#                 "messages": [{"role": "user", "content": QUESTION}],
#                 "max_completion_tokens": 100,
#             },
#             timeout=(10, 60),
#         )
#     except requests.Timeout:
#         print("Error: The OpenAI request timed out.", file=sys.stderr)
#         return 1
#     except requests.RequestException as exc:
#         print(f"Error: Could not reach the OpenAI API: {exc}", file=sys.stderr)
#         return 1

#     try:
#         data = response.json()
#     except ValueError:
#         print(
#             f"Error: The API returned an invalid JSON response (HTTP {response.status_code}).",
#             file=sys.stderr,
#         )
#         return 1

#     if not response.ok:
#         api_error = data.get("error", {}) if isinstance(data, dict) else {}
#         message = api_error.get("message") if isinstance(api_error, dict) else None
#         print(
#             f"Error: OpenAI API returned HTTP {response.status_code}"
#             + (f": {message}" if message else "."),
#             file=sys.stderr,
#         )
#         return 1

#     if isinstance(data, dict) and data.get("error"):
#         error = data["error"]
#         message = error.get("message") if isinstance(error, dict) else str(error)
#         print(f"Error: OpenAI API returned an error: {message}", file=sys.stderr)
#         return 1

#     try:
#         answer = data["choices"][0]["message"]["content"]
#     except (KeyError, IndexError, TypeError):
#         print("Error: The API response did not contain a chat completion.", file=sys.stderr)
#         return 1

#     if not isinstance(answer, str):
#         print("Error: The API response contained no text answer.", file=sys.stderr)
#         return 1

#     print("-" * 40)
#     print(answer)
#     print("-" * 40)
#     return 0


# if __name__ == "__main__":
#     sys.exit(main())


#======== 03 With Open AI Lang Chain SDK ================

# chat_model = ChatOpenAI(
#     model_name="gpt-5.6-luna",
#     openai_api_key=API_KEY,
#     max_tokens=100,
#     temperature=0.7,
#     request_timeout=60,
# )

# response = chat_model.invoke([{"role": "user", "content": QUESTION}])

# print("-" * 40)
# print(response.content)
# print("-" * 40)