from config import chat_model , rule
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from corpus import DOCS

QUESTION = "I'm growing Bg 300 paddy under irrigation in the Dry Zone. Exacltly how much urea should I apply, and what times? Give me schedule in KG per hectare."

model = chat_model() 


# rule("Ask it Threee Times.")
# print(QUESTION)

# for attempt in (1,2,3):
#     print(f"Attempt {attempt}:"+ "_" *50 )
#     print(model.invoke(messages).text)


rule("COPY THE DOC INTO PROMPT.")
facts = "\n\n".join(f"[{d['source']}]\n{d['text']}" for d in DOCS)

messages = [
    SystemMessage(content="You an advisor for Sri Lankan paddy farmers. Answer ONLY from the passages below.Quote exact figures and cite the source in prabkets\n\n" + facts),
    HumanMessage(content=QUESTION)
]


print(model.invoke(messages).text)

