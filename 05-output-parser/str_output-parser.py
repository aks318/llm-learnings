from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="""
        Summarize the text below.

        STRICT RULES:
        - Output exactly 2 short sentences.
        - Use no more than 30 words in total.
        - Do not include a heading, introduction, or conclusion.
        - Return only the summary.

        Text:
        {text}
    """,
    input_variables = ["text"]
)

# prompt1 = template1.invoke({"topic":  "black hole"})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({"text":  result.content})

# result2 = model.invoke(prompt2)


# print(result2.content)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":  "black hole"})

print(result)