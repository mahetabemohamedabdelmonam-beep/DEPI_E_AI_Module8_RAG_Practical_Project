"""Read local policy documents. These are synthetic training documents."""
from pathlib import Path

SUPPORTED = {".txt", ".md", ".pdf"}


def load_document(path: Path) -> list[dict]:
    if path.suffix.lower() not in SUPPORTED:
        return []
    if path.suffix.lower() == ".pdf":
        import fitz  # installed by pymupdf; supports text-based PDFs
        with fitz.open(path) as pdf:
            pages = [{"page": index + 1, "text": page.get_text()}
                     for index, page in enumerate(pdf)]
        return [p for p in pages if p["text"].strip()]
    text = path.read_text(encoding="utf-8")
    return [{"page": 1, "text": text}] if text.strip() else []


def iter_department_files(root: Path, department: str):
    if department not in {"hr", "accounting", "legal:","it"}:
        raise ValueError("Unsupported department")
    folder = root / department
    if not folder.is_dir():
        return
    yield from sorted(p for p in folder.iterdir()
                      if p.is_file() and p.suffix.lower() in SUPPORTED)



