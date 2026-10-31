import sys
from pathlib import Path

root_dir= Path(__file__).resolve().parents[1]

sys.path.append(str(root_dir))

from app.rag.ingestion import iter_department_files, load_document

def main():
    data_dir=root_dir/"data"/"raw"
    print("---testing iter department files for it--")
    it_files=list(iter_department_files(data_dir,"it"))
    for f in it_files:
        print(f"Found:{f.name}")

    if it_files:
        print("\n--- Testing Load_decoment ---")
        docs = load_document(it_files[0])

        if docs: 
            print (f"Page Number: {docs[0]['page']}")
            print (f"Text Preview: {docs[0]['text'][:150]}...")

if __name__ == "__main__":
    main()