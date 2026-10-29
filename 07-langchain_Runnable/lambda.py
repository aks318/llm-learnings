from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")
parser = StrOutputParser()

def wordCountFun(joke : str):
    return len(joke.split())

template1 = PromptTemplate(
    template="tell me a good joke about ai"
)

joke_gen_chain = RunnableSequence(template1, model, parser)

parallel = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "word_count": RunnableLambda(wordCountFun)
    }
)

chain = RunnableSequence(joke_gen_chain, parallel)

print(chain.invoke({}))