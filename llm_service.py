from gpt4all import GPT4All

# Load GPT4All once (when service starts)
model_path = r"A:\projet_Irad\chatbot\gpt4all-falcon-newbpe-q4_0.gguf"
gpt4all_model = GPT4All(model_path)

def generate_answer(question, retrieved_texts):
    context = "\n".join(retrieved_texts)
    prompt = f"Use the following medical information to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    with gpt4all_model.chat_session():
        return gpt4all_model.generate(prompt, max_tokens=200)
