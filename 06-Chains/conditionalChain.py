from google.auth import default
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

model = ChatOllama(model = "qwen3.8")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback as either Positive or Negative.

Feedback: {feedback}

Rules:
- Output exactly one word: Positive or Negative.
- Do not provide explanations, punctuation, or additional text.
""",
    input_variables=["feedback"]
)

classifierChain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

branch_chain =  RunnableBranch(
    (lambda x: x == "Positive" , prompt2 | model | parser),
    (lambda x: x == "Negative" , prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find the sentiment"),
)


classifierChain = prompt1 | model | parser

chain = classifierChain | branch_chain
result = chain.invoke({
    "feedback" : "This is a terrible phone"
})

print(result)



