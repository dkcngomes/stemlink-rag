# Developer : @dkcngomes

from dotenv import load_dotenv
from pathlib import Path
from langchain.chat_models import init_chat_model

project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env")

CHAT_MODEL_RAW = "gpt-5.6-luna"
CHAT_MODEL = f"openai:{CHAT_MODEL_RAW}"

def chat_model(**kwargs):
  return init_chat_model( CHAT_MODEL, **kwargs) 


def rule(title: str = "") -> None:
  """
  Section heading , so the script reads like a lesson while it runs.
  """
  print("\n" + "=" * 70)
  if title:
        print(f" {title} ")
        print("-" * 70)
