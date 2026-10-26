# Company Policy RAG System - Usage Guide

## Overview

This system allows you to query company policy documents using Retrieval-Augmented Generation (RAG). It automates the entire process from PDF processing to answering questions.

## Prerequisites

Before using the system, ensure you have:

1. **Ollama installed** - The system uses Ollama for local LLM operations
2. **Required models pulled** - Run these commands in your terminal:
   ```
   ollama pull nomic-embed-text
   ollama pull llama3.2:1b
   ```

## Step-by-Step Usage

### 1. Prepare Your Documents
- Place all PDF documents in the `documents/` folder
- The system will automatically process the first PDF it finds

### 2. Run the Complete Workflow
```bash
python run_rag_workflow.py
```

This script will:
1. Extract text from your PDF files
2. Chunk the extracted text 
3. Ingest the chunks into ChromaDB for semantic search
4. Launch the interactive query interface

### 3. Ask Questions
Once launched, you can ask questions like:
- "What are the vacation policies?"
- "How do I submit expense reports?"
- "What is the code of conduct?"

The system will provide answers based only on your company documents and cite relevant sections.

## Understanding the Components

### File Structure
- `run_rag_workflow.py` - Main automation script
- `extract_text.py` - PDF text extraction
- `chunk_text.py` - Text chunking for semantic search  
- `ingest.py` - Database ingestion (ChromaDB)
- `rag.py` - Query interface and answer generation
- `documents/` - Input PDF files
- `chroma_db/` - Persisted database storage

### Key Features
- Semantic search of documents using embeddings
- Automatic chunking with overlap for context preservation
- Chunk citation in answers (e.g., "According to [Chunk 5]...")
- Error handling and graceful degradation
- Interactive query interface

## Troubleshooting

### Common Issues
1. **"No PDF files found"** - Place your PDFs in the `documents/` folder
2. **"Model not found"** - Ensure you've pulled the required Ollama models:
   ```
   ollama pull nomic-embed-text
   ollama pull llama3.2:1b
   ```
3. **Permission errors** - Make sure scripts have execution permissions:
   ```bash
   chmod +x *.py
   ```

### System Requirements
- Python 3.7+
- At least 4GB RAM for embedding operations
- Ollama running locally

## Example Query Session

```
Company Policy RAG — type 'exit' to quit.

You: What is the policy on remote work?
Assistant: According to [Chunk 12], employees may work remotely up to 3 days per week with management approval. The policy requires that remote workers maintain availability during core business hours (9AM-5PM) and have a dedicated workspace.

You: How do I submit a time off request?
Assistant: Based on [Chunk 8], you must submit time off requests through the HR portal at least 2 weeks in advance for planned absences. Requests are reviewed by your direct manager, who has 3 business days to approve or deny the request.
```

## Customization

### Adjusting Parameters
You can modify these values in `rag.py`:
- `TOP_K` - Number of document chunks to retrieve (default: 3)  
- `EMBEDDING_MODEL` - Model for text embedding (default: "nomic-embed-text")
- `CHAT_MODEL` - Model for answer generation (default: "llama3.2:1b")

### Changing Chunk Size
Modify values in `ingest.py`:
- `CHUNK_SIZE` - Size of text chunks (default: 1000)
- `CHUNK_OVERLAP` - Overlap between chunks (default: 200)