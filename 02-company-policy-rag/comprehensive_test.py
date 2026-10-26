#!/usr/bin/env python3

"""
Comprehensive test script for RAG functionality using actual database.
"""

import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """Main test function"""
    
    try:
        from rag import retrieve_chunks, generate_answer
        
        # Test queries
        test_queries = [
            "What is the gross annual salary?",
            "What are the learning incentives?",
            "When will I receive the joining letter?",
            "What is the position offered?"
        ]
        
        print("Running comprehensive RAG tests...")
        print("=" * 50)
        
        for i, question in enumerate(test_queries, 1):
            print(f"\nTest {i}: {question}")
            print("-" * 30)
            
            # Retrieve chunks
            chunks = retrieve_chunks(question)
            
            if not chunks:
                print("No relevant information found.")
                continue
            
            print(f"Found {len(chunks)} relevant chunk(s):")
            for j, chunk in enumerate(chunks, 1):
                print(f"  Chunk {j}:")
                # Show first 200 characters of each chunk
                content = chunk.split('\n', 1)[1] if '\n' in chunk else chunk
                print(f"    {content[:200]}{'...' if len(content) > 200 else ''}")
            
            # Generate answer
            answer = generate_answer(question, chunks)
            print(f"Answer: {answer}")
            print()
        
        print("=" * 50)
        print("✓ All tests completed successfully!")
        
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()