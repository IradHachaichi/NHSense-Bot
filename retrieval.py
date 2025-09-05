import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path of retrieval.py

# Load index + texts
index_path = os.path.join(BASE_DIR, "conditions.index")
index = faiss.read_index(index_path)

texts_path = os.path.join(BASE_DIR, "condition_texts.pkl")
with open(texts_path, "rb") as f:
    condition_texts = pickle.load(f)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_condition(question, top_k=1):
    q_emb = embed_model.encode([question], convert_to_tensor=False).astype("float32")
    distances, indices = index.search(q_emb, top_k)
    return [condition_texts[i] for i in indices[0]]
