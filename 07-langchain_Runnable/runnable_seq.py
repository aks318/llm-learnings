from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")
parser = StrOutputParser()

template = PromptTemplate(
    template= "Tell me about: {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template= "Summarize below topic in 1 line: {topic}",
    input_variables=["topic"]
)

chain = RunnableSequence(template, model, parser, template2, model, parser)

result = chain.invoke({"topic": "Climate"})

print(result)