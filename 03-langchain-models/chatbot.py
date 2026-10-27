from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model = "llama3.2:1b")

chat_his = [
    SystemMessage(
    content="""
    You are a factual AI assistant.

    Rules:
    1. Answer using information you know with reasonable confidence.
    2. Never invent facts, names, dates, or statistics.
    3. If you do not know the answer, respond exactly:
       I don't know.
    4. If the question requires information you cannot access,
       clearly state that you do not have that information.
    5. Keep your answers concise.
    """
)
]

while True:
    userInput = input("User: ").strip()
    if userInput == "Exit":
        break
    chat_his.append(HumanMessage(content= userInput))

    result = model.invoke(chat_his)
    chat_his.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")