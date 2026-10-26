#!/usr/bin/env python3
"""
Complete workflow automation script for company policy RAG system.
This script runs all necessary steps in sequence: PDF extraction, text chunking,
data ingestion into ChromaDB, and finally the RAG query interface.
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path so we can import other scripts
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def run_extraction():
    """Run the text extraction from PDF script"""
    print("Step 1: Extracting text from PDF...")
    
    # Check if documents folder exists
    documents_dir = current_dir / "documents"
    if not documents_dir.exists():
        print("Error: Documents directory does not exist. Please create a 'documents' folder and place your PDF files there.")
        return False
    
    # Check for PDF files
    pdf_files = list(documents_dir.glob("*.pdf"))
    if not pdf_files:
        print("Error: No PDF files found in the documents folder.")
        print("Please place at least one PDF file in the 'documents' folder and run this script again.")
        return False
    
    try:
        # Execute the extraction script directly
        import extract_text
        print("✓ Text extraction complete")
        return True
    except Exception as e:
        print(f"✗ Error during text extraction: {e}")
        return False

def run_ingestion():
    """Run the data ingestion script into ChromaDB"""
    print("Step 2: Ingesting data into ChromaDB...")
    
    try:
        # Import and run the ingestion script
        from ingest import main as ingest_main
        ingest_main()
        print("✓ Data ingestion complete")
        return True
    except Exception as e:
        print(f"✗ Error during data ingestion: {e}")
        return False

def run_rag():
    """Run the RAG query interface"""
    print("Step 3: Starting RAG system...")
    
    try:
        # Import and run the RAG script
        from rag import main as rag_main
        rag_main()
        print("RAG system terminated.")
    except Exception as e:
        print(f"✗ Error during RAG interaction: {e}")

def main():
    """Run the complete workflow"""
    print("Company Policy RAG Workflow")
    print("=" * 40)
    
    # Check if we have the required directory structure
    documents_dir = current_dir / "documents"
    if not documents_dir.exists():
        print("Creating documents directory...")
        documents_dir.mkdir(exist_ok=True)
        print("Please place your PDF documents in the 'documents' folder and run this script again.")
        return
    
    # Run all steps in sequence
    try:
        if run_extraction():
            if run_ingestion():
                print("\nStarting interactive RAG interface...")
                run_rag()
            else:
                print("Ingestion failed. Workflow stopped.")
        else:
            print("Extraction failed. Workflow stopped.")
    except KeyboardInterrupt:
        print("\nWorkflow interrupted by user.")
    except Exception as e:
        print(f"Unexpected error during workflow: {e}")

if __name__ == "__main__":
    main()