from langchain_ollama import ChatOllama, OllamaEmbeddings

# llm = ChatOllama(
#     model="qwen3.8:latest ",
#     temprature = 1,
# )

# response = llm.invoke("What is Langchain? Explain in two sentences.")

# print(response)

embeddings = OllamaEmbeddings(model="nomic-embed-text", dimensions=5)

docs = [
    "Hello",
    "hi", 
    "its me",
    "dog"
]

vector1 = embeddings.embed_documents(docs)

print(vector1)
