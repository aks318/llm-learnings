from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

model = ChatOllama(
    model = "llama3.2:1b"
)

@tool
def multiply(a: int, b: int) -> int:
    """"Multiply two numbers"""
    print("tool called")
    return a*b

messages = [HumanMessage("multiple 3 and 5")]

result = multiply.invoke({"a" : 3, "b" :2})

model_with_tools = model.bind_tools([multiply])

result =  model_with_tools.invoke("multiple 3 and 5")

messages.append(result)

toolMsg = multiply.invoke(result.tool_calls[0])

messages.append(toolMsg)

print(model.invoke(messages))
