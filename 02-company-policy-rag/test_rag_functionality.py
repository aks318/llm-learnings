#!/usr/bin/env python3

"""
Simple test script to verify RAG functionality without interactive input.
"""

import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def test_retrieve_chunks():
    """Test the retrieve_chunks function with a sample question"""
    
    try:
        from rag import retrieve_chunks
        
        # Test with a simple question about salary
        question = "What is the gross annual salary?"
        
        print(f"Testing retrieval for: '{question}'")
        chunks = retrieve_chunks(question)
        
        if not chunks:
            print("No chunks retrieved.")
            return False
            
        print(f"Retrieved {len(chunks)} chunks:")
        for i, chunk in enumerate(chunks):
            print(f"\nChunk {i+1}:")
            print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
            
        return True
        
    except Exception as e:
        print(f"Error in retrieve_chunks: {e}")
        return False

def test_generate_answer():
    """Test the generate_answer function with sample chunks"""
    
    try:
        from rag import generate_answer
        
        # Sample chunks for testing
        chunks = [
            "[Chunk 1]\nYour gross salary including all benefits will be `3,36,875/- per annum, as per the terms and conditions set out herein.",
            "[Chunk 2]\nOver and above this, you will also be eligible for Learning Incentives (Readiness Incentive and/or Competency Incentive) basis your performance in TCS Xplore Program which gives you an additional earning potential of upto Rs.60,000 during the first year."
        ]
        
        question = "What is the gross annual salary?"
        
        print(f"\nTesting answer generation for: '{question}'")
        answer = generate_answer(question, chunks)
        
        print("Generated Answer:")
        print(answer)
        
        return True
        
    except Exception as e:
        print(f"Error in generate_answer: {e}")
        return False

if __name__ == "__main__":
    print("Testing RAG functionality...")
    
    success1 = test_retrieve_chunks()
    success2 = test_generate_answer()
    
    if success1 and success2:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed.")