from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="llama3.2:1b")
parser = StrOutputParser()

template1 = PromptTemplate(
    template= "Create a tweet about: {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template= "Create a linkdin about: {topic}",
    input_variables=["topic"]
)

chain = RunnableParallel({
    "tweet" : RunnableSequence(template1, model, parser),
    "linkdin" : RunnableSequence(template1, model, parser)
})

result = chain.invoke("Virat kohli")

print(result)
