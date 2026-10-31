import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from app.rag.chunking import chunk_text


def main():
    text = (
        "Artificial intelligence is transforming how companies operate. "
        "Modern systems can read documents, answer questions, and automate routine tasks. "
        "Retrieval augmented generation helps models use private company data safely."
    )

    chunk_size = 50
    overlap = 15

    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

    print("--- Chunks ---")
    for i, c in enumerate(chunks):
        print(i, repr(c))

    print("\n--- Overlap check ---")
    print("End of chunk 0:  ", repr(chunks[0][-overlap:]))
    print("Start of chunk 1:", repr(chunks[1][:overlap]))
    print("Shared characters:", overlap)
    print("Overlap matches:", chunks[0][-overlap:] == chunks[1][:overlap])


if __name__ == "__main__":
    main()