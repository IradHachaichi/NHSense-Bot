from gpt4all import GPT4All

# Load GPT4All once (when service starts)
# TODO: Replace 'path_to_model.gguf' with the full path to your GPT4All model
model_path = r"path_to_model.gguf"
gpt4all_model = GPT4All(model_path)

def generate_answer(question, retrieved_texts):
    context = "\n".join(retrieved_texts)
    prompt = f"Use the following medical information to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    with gpt4all_model.chat_session():
        return gpt4all_model.generate(prompt, max_tokens=200)

