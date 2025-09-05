import json
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load data
with open("nhs_conditions_fixed.json", "r", encoding="utf-8") as f:
    conditions_data = json.load(f)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Build condition texts
condition_texts = []
for cond in conditions_data:
    text = cond.get("condition", "")
    for key in ["overview", "symptoms", "diagnosis", "medical-treatments", "prevention", "causes", "urgent"]:
        if key in cond:
            val = cond[key]
            text += " " + (" ".join(val) if isinstance(val, list) else val)
    condition_texts.append(text)

# Embeddings
embeddings = embed_model.encode(condition_texts, convert_to_tensor=False).astype("float32")

# Build FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# Save
faiss.write_index(index, "conditions.index")
with open("condition_texts.pkl", "wb") as f:
    pickle.dump(condition_texts, f)

print("✅ FAISS index and texts saved.")
