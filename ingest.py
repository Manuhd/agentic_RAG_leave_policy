import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def ingest_documents():
    texts = []

    for file in os.listdir("data"):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            texts.append(f.read())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_text("\n".join(texts))

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_texts(chunks, embeddings)
    db.save_local("faiss_db")

    print("✅ Documents ingested using HuggingFace embeddings")

if __name__ == "__main__":
    ingest_documents()
