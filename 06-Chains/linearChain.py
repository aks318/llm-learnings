from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")

parser = StrOutputParser()

template = PromptTemplate(
    template="Give me 2 facts about AI"
)

template2 = PromptTemplate(
    template="Out of these 2 facts:\n{text}\nGive me only 1 fact.",
    input_variables = ["text"]
)

chain = template | model | parser | template2 | model | parser

result = chain.invoke({})

print(result)

# print(chain.get_graph().print_ascii())