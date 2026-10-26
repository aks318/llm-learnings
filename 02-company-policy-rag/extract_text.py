
from pathlib import Path
from pypdf import PdfReader

def main():
    # Locate the documents folder
    PROJECT_DIR = Path(__file__).parent
    DOCUMENTS_DIR = PROJECT_DIR / "documents"

    # Find PDF files
    pdf_files = list(DOCUMENTS_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in {DOCUMENTS_DIR}"
        )

    # Use the first PDF for now
    pdf_path = pdf_files[0]

    print(f"Reading PDF: {pdf_path.name}")

    reader = PdfReader(pdf_path)

    all_text = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        all_text.append(text)

        print(f"Extracted page {page_number}")

    # Combine all pages into one string
    full_text = "\n\n".join(all_text)

    # Save extracted text to a file
    output_path = PROJECT_DIR / "extracted_text.txt"
    output_path.write_text(full_text, encoding="utf-8")

    print(f"\nTotal pages: {len(reader.pages)}")
    print(f"Total characters: {len(full_text)}")
    print(f"Extracted text saved to: {output_path}")
    print("\nPreview:\n")
    print(full_text[:2000])

if __name__ == "__main__":
    main()
