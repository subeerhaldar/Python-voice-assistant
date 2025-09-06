import os
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

class Retriever:
    def __init__(self, docs_path="data/docs"):
        self.docs_path = docs_path
        os.makedirs(self.docs_path, exist_ok=True)
        self.docs = self._load_docs()
        self.embeddings = OllamaEmbeddings(model="llama3")
        self.db = FAISS.from_documents(self.docs, self.embeddings)

    def _load_docs(self):
        docs = []
        for fname in os.listdir(self.docs_path):
            if fname.endswith(".txt") or fname.endswith(".md"):
                with open(os.path.join(self.docs_path, fname), encoding="utf-8") as f:
                    docs.append(Document(page_content=f.read(), metadata={"source": fname}))
        return docs

    def search(self, query, k=5):
        return self.db.similarity_search(query, k=k)