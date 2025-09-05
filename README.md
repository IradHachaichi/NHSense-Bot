# NHSense-Bot
NHS ChatBot is an intelligent chatbot designed to help users find reliable information about medical conditions listed on the NHS website. It uses Retrieval-Augmented Generation (RAG) to combine information retrieval with natural language generation, providing accurate and context-aware responses to user queries.
# 🏥 NHSense Bot

**NHSense Bot** is a chatbot that provides reliable medical information based on the [NHS Conditions](https://www.nhs.uk/conditions/) website.  
It combines **retrieval-augmented generation (RAG)** with embeddings and a lightweight language model to answer user questions quickly and accurately.  

---

## 🚀 Project Overview

- **Data source:** Scraped from [NHS Conditions](https://www.nhs.uk/conditions/)  
- **Data embedding:** `all-MiniLM-L6-v2` from `SentenceTransformers`  
- **Indexing:** FAISS is used to index embeddings for fast retrieval  
- **Language model:** `gpt4all-falcon-newbpe-q4_0.gguf` (runs locally for performance reasons)  
- **API framework:** FastAPI to serve the chatbot  

---

## 📂 Project Structure

### 1. `build_index.py`
- Loads the NHS dataset (`nhs_conditions_fixed.json`)  
- Creates embeddings with `all-MiniLM-L6-v2`  
- Builds a FAISS index for similarity search  
- Saves:
  - `conditions.index` (FAISS index)  
  - `condition_texts.pkl` (raw condition texts)  

**Run this script before starting the app:**
```bash
python build_index.py

