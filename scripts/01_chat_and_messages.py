from config import chat_model , rule
from langchain.messages import SystemMessage, HumanMessage

QUESTION = "Name the two paddy cultivation seasons in Sri Lanka."
QUESTION2 = "What is Bg 300?"

model = chat_model()
messages = [
    SystemMessage(content="You are a terse agricultural advisor for Sri Lankan farmers."),
    HumanMessage(content=QUESTION2)
]
response = model.invoke(messages)

# rule("1.Messages Have Roles")
# print(response.content)

# rule("2.New follow-up question for Bg 300")
# response = model.invoke([HumanMessage(content="How long does it takes to mature?")])
# print(response.content)

rule("3.We need to maintain list of messages for context")
messages.append(response)
messages.append(HumanMessage(content="How long does it takes to mature?"))

for m in messages:
    print(f" {type(m).__name__:14s} {m.text[:52]!r}")

followup = model.invoke(messages)
print("-" * 70)
print(followup.content)