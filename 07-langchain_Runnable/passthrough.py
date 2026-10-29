from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")
parser = StrOutputParser()

template1 = PromptTemplate(
    template="tell me a good joke about ai"
)

template2 = PromptTemplate(
    template="Explain me the below joke: {joke}",
    input_variables=["joke"]
)

joke_gen_chain = RunnableSequence(template1, model, parser)

parallerChain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explain": RunnableSequence(template2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallerChain)

print(final_chain.invoke({}))