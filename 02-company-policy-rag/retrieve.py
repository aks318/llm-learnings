
from pathlib import Path

import chromadb
import ollama

PROJECT_DIR = Path(__file__).parent
DB_DIR = PROJECT_DIR / "chroma_db"

EMBEDDING_MODEL = "nomic-embed-text"
COLLECTION_NAME = "company_policy"


def retrieve_chunks(question: str, top_k: int = 3):
    client = chromadb.PersistentClient(path=str(DB_DIR))

    collection = client.get_collection(
        name=COLLECTION_NAME
    )

    # Convert the user's question into an embedding.
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=question,
    )
    question_embedding = response["embeddings"][0]

    # Find the most semantically similar document chunks.
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    return results


def main():
    question = input("Ask a question about your offer letter: ").strip()

    if not question:
        print("Please enter a question.")
        return

    results = retrieve_chunks(question)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    print("\nRelevant chunks:\n")

    for index, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances),
        start=1,
    ):
        print(f"--- Result {index} ---")
        print(f"Chunk index: {metadata['chunk_index']}")
        print(f"Cosine distance: {distance:.4f}")
        print(document)
        print()


if __name__ == "__main__":
    main()
