#!/usr/bin/env python3

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

    # Filter out chunks that seem like headers or metadata
    filtered_chunks = []
    for chunk in chunks:
        # Skip chunks that are likely headers or don't contain meaningful content
        lines = chunk.split('\n')
        if len(lines) < 3:
            # Likely a header or metadata, skip it
            continue
            
        # If the chunk contains mostly numbers or special characters,
        # it might be a page number or formatting info
        content_lines = [line for line in lines[1:] if line.strip()]
        if not content_lines:
            continue
            
        filtered_chunks.append(chunk)
    
    context = "\n\n".join(filtered_chunks)

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
                    "If the answer is not present in the document, say so clearly. "
                    "Focus on providing factual information about employment terms, salary, and benefits."
                )
            },
            {
                "role": "user",
                "content": f"Question: {question}\n\nContext: {context}"
            }
        ]
    )
    
    return response['message']['content']

def main():
    print("Enhanced Company Policy RAG System")
    print("=" * 40)
    print("Ask questions about your offer letter (type 'exit' to quit)")
    
    while True:
        try:
            question = input("\nYou: ").strip()
            
            if not question:
                continue
                
            if question.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            chunks = retrieve_chunks(question)
            
            if not chunks:
                print("No relevant information found.")
                continue
            
            answer = generate_answer(question, chunks)
            print(f"Assistant: {answer}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()