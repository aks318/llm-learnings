
from pathlib import Path

import chromadb
import ollama

PROJECT_DIR = Path(__file__).parent
DB_DIR = PROJECT_DIR / "chroma_db"

EMBEDDING_MODEL = "nomic-embed-text"
CHAT_MODEL = "llama3.2:1b"
COLLECTION_NAME = "company_policy"
TOP_K = 3


def retrieve_chunks(question: str) -> list[str]:
    client = chromadb.PersistentClient(path=str(DB_DIR))

    collection = client.get_collection(
        name=COLLECTION_NAME
    )

    if collection.count() == 0:
        return []

    # Embed the question using the same model used during ingestion.
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=question,
    )
    question_embedding = response["embeddings"][0]

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=min(TOP_K, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0] or []
    metadatas = results["metadatas"][0] or []

    # Include chunk identifiers so answers can be traced back.
    chunks = []

    for document, metadata in zip(documents, metadatas):
        chunk_index = metadata["chunk_index"]
        chunks.append(
            f"[Chunk {chunk_index}]\n{document}"
        )

    return chunks



def generate_answer(question: str, chunks: list[str]) -> str:
    if not chunks:
        return "I couldn't find relevant information in the document."

    context = "\n\n".join(chunks)

    response = ollama.chat(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a company policy assistant. "
                    "Answer the user's question using only the provided context. "
                    "Do not repeat the context or list the chunks. "
                    "Give a direct, concise answer in natural language. "
                    "If the answer is not present in the context, say so. "
                    "Include a chunk citation only when it supports your answer. "
                    "If the provided context does not contain sufficient information to answer the question, respond with: 'The available document excerpts do not provide sufficient information to answer the question.'"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n{context}\n\n"
                    f"Question: {question}\n\n"
                    "Provide only the answer, not the retrieved context."
                ),
            },
        ],
    )

    return response["message"]["content"]


def main():
    print("Company Policy RAG — type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            chunks = retrieve_chunks(question)
            answer = generate_answer(question, chunks)
            print(f"\nAssistant: {answer}")

        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
