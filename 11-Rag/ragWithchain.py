from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama , OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

video_id = "Gfr50f6ZBvo"

try:
    transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    transcript = " ".join(chunk.text for chunk in transcript_list)

except TranscriptsDisabled:
    print("No transcript available")


splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
chunks = splitter.create_documents([transcript])

embedding = OllamaEmbeddings(model = "nomic-embed-text:latest")

vector_store = FAISS.from_documents(chunks, embedding)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k" : 4})


model = ChatOllama(
    model="llama3.2:1b"
)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


def formatDoc(docs):
    return "\n\n".join(doc.page_content for doc in docs)

parallel_chain = RunnableParallel({
    "question" : RunnablePassthrough(),
    "context" : retriever | RunnableLambda(formatDoc)
})

parser = StrOutputParser()

main_chain = parallel_chain | prompt | model |parser

result = main_chain.invoke("Can you summarize the video")

print(result.content)