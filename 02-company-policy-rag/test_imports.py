#!/usr/bin/env python3
"""
Test script to verify all imports work properly.
"""

import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    import chromadb
    print("✓ ChromaDB imported successfully")
    
    import ollama
    print("✓ Ollama imported successfully")
    
    from rag import retrieve_chunks, generate_answer
    print("✓ RAG functions imported successfully")
    
    print("\nAll imports successful!")
    
except Exception as e:
    print(f"✗ Import error: {e}")
    import traceback
    traceback.print_exc()