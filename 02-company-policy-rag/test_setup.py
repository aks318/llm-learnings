#!/usr/bin/env python3
"""
Simple test script to verify the RAG system setup is correct.
"""

import sys
from pathlib import Path

# Test that all required imports work
def test_imports():
    try:
        import chromadb
        import ollama
        from pypdf import PdfReader
        print("✓ All required imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_directories():
    current_dir = Path(__file__).parent
    required_dirs = ["documents", "chroma_db"]
    
    for dir_name in required_dirs:
        dir_path = current_dir / dir_name
        if not dir_path.exists():
            print(f"✓ Creating directory: {dir_name}")
            dir_path.mkdir(exist_ok=True)
        else:
            print(f"✓ Directory exists: {dir_name}")
    
    return True

def main():
    print("Testing RAG System Setup")
    print("=" * 30)
    
    success = True
    success &= test_imports()
    success &= test_directories()
    
    if success:
        print("\n✓ Setup verification complete - all systems ready!")
    else:
        print("\n✗ Setup verification failed")
        sys.exit(1)

if __name__ == "__main__":
    main()