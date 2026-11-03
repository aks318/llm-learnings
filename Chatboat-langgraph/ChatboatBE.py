from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages

from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated

from langgraph.checkpoint.memory import MemorySaver

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

llm = ChatOllama(model= "llama3.2:1b")

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

checkPointer = MemorySaver()
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkPointer)

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

for message_chunk, metadata in chatbot.stream(
    {"messages": [HumanMessage(content="What is the recipe to make pasta?")]}, 
    config=CONFIG, 
    stream_mode="messages"
):
    if message_chunk.content:
        print(message_chunk.content, end=" ", flush=True)