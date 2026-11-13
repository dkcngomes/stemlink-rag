# Developer : @dkcngomes
from config import chat_model , rule
from weather import get_forecast
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.runtime import CONF , CONFIG_KEY_RUNTIME, DEFAULT_RUNTIME
from langgraph.prebuilt import ToolNode

QUESTION = "Pollonaruwa rain forcast for the next 24 hours in mm?"
model = chat_model(reasoning_effort="none") 

messages = [
    SystemMessage(content="You are an advisor for Sri Lankan Paddy Farmers."),
    HumanMessage(content=QUESTION),
    AIMessage(content=""),
]

model_with_tools = model.bind_tools([get_forecast])

#rule("TOOLS CAN BE CALLED TO THE MODEL")
# print(get_forecast) # returns tool function definition 
#print(get_forecast.func("Gampaha")) #call out a function with a @tool decorator, and it will return the result of the function call.

reply = model_with_tools.invoke(messages)
messages.append(reply) # appending the model output to the messages list, so that it can be used for further reasoning. 

#rule("LETS show the model of tools.")
#print(reply.text) # returns the model output with the tool call and the result of the tool call.

# for tc in reply.tool_calls:
#     print("  ", tc) # returns the tool calls made by the model.

rule("LETS execute the tool calls that model makes.")

tool_node = ToolNode([get_forecast])
NO_GRAPH = {CONF: {CONFIG_KEY_RUNTIME: DEFAULT_RUNTIME}} # we are not using a graph here, so we
observations = tool_node.invoke(messages, config=NO_GRAPH) # executes the tool calls made by the model.

messages.append(observations[0]) # appending the observations made by the tool calls to the messages list, so that it can be used for further reasoning.

##print("Observations:", observations) # returns the observations made by the tool calls.
#print(messages) # returns the messages list with the model output and the observations made by the tool calls.

final_reply = model_with_tools.invoke(messages) # final reasoning by the model with the observations made by the tool calls.
print("Final Reply:", final_reply.text) # returns the final reply by the model with the observations
