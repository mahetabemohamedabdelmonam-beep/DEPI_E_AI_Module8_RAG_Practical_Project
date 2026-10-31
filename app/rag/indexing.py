"""Build/update vector collections from files inside data/raw/<department>."""
from hashlib import sha256
from pathlib import Path
from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.rag.ingestion import iter_department_files, load_document
from app.rag.vector_store import get_collection


def index_department(root: Path, department: str) -> dict:
    collection = get_collection(department)
    indexed_files, indexed_chunks = 0, 0
    for path in iter_department_files(root, department):
        source = f"{department}/{path.name}"
        # Re-indexing one document replaces its previous chunks.
        if collection.count():
            collection.delete(where={"source": source})
        documents, metadatas, ids = [], [], []
        for page in load_document(path):
            for chunk_idx, chunk in enumerate(chunk_text(page["text"])):
                uid = sha256(f"{source}:{page['page']}:{chunk_idx}".encode()).hexdigest()
                ids.append(uid)
                documents.append(chunk)
                metadatas.append({"source": source, "page": page["page"],
                                  "chunk_index": chunk_idx, "department": department})
        if documents:
            collection.upsert(ids=ids, embeddings=embed_texts(documents),
                              documents=documents, metadatas=metadatas)
            indexed_files += 1
            indexed_chunks += len(documents)
    return {"department": department, "files": indexed_files, "chunks": indexed_chunks}
