
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
INPUT_FILE = PROJECT_DIR / "extracted_text.txt"
OUTPUT_FILE = PROJECT_DIR / "chunks.txt"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def split_into_chunks(text: str) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # Move forward, keeping some text from the previous chunk.
        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    text = INPUT_FILE.read_text(encoding="utf-8")

    chunks = split_into_chunks(text)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        for index, chunk in enumerate(chunks, start=1):
            file.write(f"\n{'=' * 30}\n")
            file.write(f"CHUNK {index}\n")
            file.write(f"{'=' * 30}\n")
            file.write(chunk)
            file.write("\n")

    print(f"Total characters: {len(text)}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Chunk size: {CHUNK_SIZE} characters")
    print(f"Chunk overlap: {CHUNK_OVERLAP} characters")
    print(f"Saved chunks to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
