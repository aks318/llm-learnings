from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

model = ChatOllama(model = "llama3.2:1b")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "Explain me about {topic}")
])

chat_history = []

with open("chat_history.txt") as f:
    chat_history.extend(f.readline())

prompt = chat_template.invoke({"domain": "cricket", "chat_history": chat_history, "topic": "Rules"})

print(prompt)

result = model.invoke(prompt)
print(result.content)