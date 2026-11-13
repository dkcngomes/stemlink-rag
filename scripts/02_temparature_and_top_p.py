# Developer : @dkcngomes
from config import chat_model , rule
from langchain.messages import SystemMessage, HumanMessage, AIMessage

QUESTION = "Name the two paddy cultivation seasons in Sri Lanka."
QUESTION2 = "What is Bg 300?"

cold_t = chat_model(reasoning_effort ="none", temperature=0.0) # to make not to be too determenestic - set temparature to 0.0
hot_t = chat_model(reasoning_effort ="none", temperature=2.0) # to make system more probabilistic / Stochastic - set temparature to 2.0

cold_p = chat_model(reasoning_effort ="none", temperature=0.0, top_p=0.1) # to make not to be too determenestic - set temparature to 0.0
hot_p = chat_model(reasoning_effort ="none", temperature=0.0, top_p=1.0) # to make system more probabilistic / Stochastic - set temparature to 2.0


messages = [
    SystemMessage(content="You are a terse agricultural advisor for Sri Lankan farmers."),
    HumanMessage(content=QUESTION2)
]

response = hot_p.invoke(messages)

rule("3.Temperature and Top P - Reasonning models can not have temparature")

messages.append(response)
messages.append(HumanMessage(content="How long does it takes to mature?"))

print("Sending," , len(messages), "messages to model:")
for m in messages:
    print(f" {type(m).__name__:14s} {m.text[:100]!r}")

followup = hot_p.invoke(messages)
print("-" * 70)
print(followup.content)




