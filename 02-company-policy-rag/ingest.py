
from pathlib import Path

import chromadb
import ollama

PROJECT_DIR = Path(__file__).parent
INPUT_FILE = PROJECT_DIR / "extracted_text.txt"
DB_DIR = PROJECT_DIR / "chroma_db"

EMBEDDING_MODEL = "nomic-embed-text"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def split_into_chunks(text: str) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"File not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")
    chunks = split_into_chunks(text)

    if not chunks:
        raise ValueError("No text chunks found in the input file.")

    # Create a persistent local ChromaDB database.
    client = chromadb.PersistentClient(path=str(DB_DIR))

    collection = client.get_or_create_collection(
        name="company_policy",
        metadata={"hnsw:space": "cosine"},
    )

    # Rebuild the collection on each run to avoid duplicate records.
    existing_ids = collection.get()["ids"]
    if existing_ids:
        collection.delete(ids=existing_ids)

    for start in range(0, len(chunks), 32):
        batch = chunks[start:start + 32]

        embeddings = []
        for chunk in batch:
            response = ollama.embed(
                model=EMBEDDING_MODEL,
                input=chunk,
            )
            embeddings.append(response["embeddings"][0])

        ids = [
            f"chunk_{start + index}"
            for index in range(len(batch))
        ]

        metadatas = [
            {"chunk_index": start + index}
            for index in range(len(batch))
        ]

        collection.add(
            ids=ids,
            documents=batch,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        print(f"Stored {min(start + len(batch), len(chunks))}/{len(chunks)} chunks")

    print("\nIngestion complete!")
    print(f"Total chunks stored: {collection.count()}")
    print(f"Database location: {DB_DIR}")


if __name__ == "__main__":
    main()
