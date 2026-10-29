from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embeddingModel = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

vectorStore = Chroma.from_documents(
    documents=documents,
    embedding=embeddingModel,
    collection_name="Doc"
)
retriever = vectorStore.as_retriever(search_kwargs={"k": 2})

query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)