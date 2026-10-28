from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

model = ChatOllama(model="llama3.2:1b")

schema = [
    ResponseSchema(name="Fact1", description="Fact 1 about the topic"),
    ResponseSchema(name="Fact2", description="Fact 2 about the topic"),
    ResponseSchema(name="Fact3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=["topic"],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)