"""Genuine RAG. The rag_pattern rule MUST detect this."""
import chromadb
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
store = chromadb.Client()


def build_retrieval_chain(question: str):
    """RAG: semantic_search over the vector store, then generate."""
    hits = store.query(query_texts=[question], n_results=5)
    return hits
