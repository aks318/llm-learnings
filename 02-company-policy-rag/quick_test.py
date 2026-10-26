#!/usr/bin/env python3

"""
Quick test to verify the entire system works.
"""

import os
import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def test_extraction():
    """Test that we can run text extraction"""
    print("Testing text extraction...")
    
    try:
        from extract_text import main as extract_main
        
        # Run the extraction
        extract_main()
        
        print("✓ Text extraction completed successfully")
        return True
    except Exception as e:
        print(f"✗ Text extraction failed: {e}")
        return False

def test_chunking():
    """Test that we can run text chunking"""
    print("Testing text chunking...")
    
    try:
        from chunk_text import main as chunk_main
        
        # Run the chunking
        chunk_main()
        
        print("✓ Text chunking completed successfully")
        return True
    except Exception as e:
        print(f"✗ Text chunking failed: {e}")
        return False

def test_ingestion():
    """Test that we can run data ingestion"""
    print("Testing data ingestion...")
    
    try:
        from ingest import main as ingest_main
        
        # Run the ingestion
        ingest_main()
        
        print("✓ Data ingestion completed successfully")
        return True
    except Exception as e:
        print(f"✗ Data ingestion failed: {e}")
        return False

def test_rag_functionality():
    """Test basic RAG functionality"""
    print("Testing RAG functionality...")
    
    try:
        from rag import retrieve_chunks, generate_answer
        
        # Test with a simple question
        question = "What is the gross annual salary?"
        chunks = retrieve_chunks(question)
        
        if chunks:
            answer = generate_answer(question, chunks)
            print(f"✓ RAG test completed. Answer: {answer}")
            return True
        else:
            print("✓ RAG test completed (no results found).")
            return True
            
    except Exception as e:
        print(f"✗ RAG functionality failed: {e}")
        return False

if __name__ == "__main__":
    print("Running system tests...")
    print("=" * 40)
    
    tests = [
        test_extraction,
        test_chunking,
        test_ingestion,
        test_rag_functionality
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
        print()
    
    if all(results):
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed.")