from config import chat_model , rule
from langchain.messages import SystemMessage, HumanMessage, AIMessage

QUESTION = "Name the two paddy cultivation seasons in Sri Lanka."
QUESTION2 = "What is Bg 300?"

model = chat_model() # to make not to be too determenestic - set temparature to 0.0

messages = [
    SystemMessage(content="You are a terse agricultural advisor for Sri Lankan farmers."),
    HumanMessage(content=QUESTION2)
]

response = model.invoke(messages)

rule("3.Temperature and Top P - Reasonning models can not have temparature")

messages.append(response)
messages.append(HumanMessage(content="How long does it takes to mature?"))

print("Sending," , len(messages), "messages to model:")
for m in messages:
    print(f" {type(m).__name__:14s} {m.text[:100]!r}")

followup = model.invoke(messages)
print("-" * 70)
print(followup.content)




