from fastapi import FastAPI
from retrieval import retrieve_condition
from llm_service import generate_answer

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    relevant_texts = retrieve_condition(question, top_k=1)
    answer = generate_answer(question, relevant_texts)
    return {"question": question, "answer": answer}
