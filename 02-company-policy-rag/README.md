# Company Policy RAG System

This is a Retrieval-Augmented Generation (RAG) system that allows querying company policy documents. It uses LLMs and vector databases to retrieve relevant information from policy documents.

## Features

- PDF text extraction from company policies
- Text chunking for better retrieval
- Vector embedding using Ollama
- ChromaDB for vector storage
- LLM-powered question answering

## Architecture

1. **Text Extraction**: Extracts text from PDF files in the `documents/` folder
2. **Chunking**: Divides text into manageable chunks  
3. **Ingestion**: Stores chunks in ChromaDB with embeddings
4. **Query**: Retrieves relevant chunks and generates answers using LLM

## Setup

1. Create a `documents` folder and place your PDF files there
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the workflow:
   ```bash
   python3 run_rag_workflow.py
   ```

## Files

- `run_rag_workflow.py`: Main workflow script
- `extract_text.py`: PDF text extraction
- `chunk_text.py`: Text chunking 
- `ingest.py`: Data ingestion into ChromaDB
- `retrieve.py`: Retrieval functions
- `rag.py`: Main RAG interface
- `chroma_db/`: Vector database storage

## Usage

After running the workflow, you'll be able to query the system with questions about company policies.

Example queries:
- "What is the gross annual salary?"
- "What are the learning incentives?" 
- "What position am I offered?"

## Requirements

- Python 3.8+
- Ollama
- Required Python packages (see requirements.txt)