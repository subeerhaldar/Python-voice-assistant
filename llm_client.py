import ollama
import logging

class LLMClient:
    def __init__(self, model_name, base_url):
        self.model_name = model_name
        self.base_url = base_url

    def ask(self, prompt, context):
        # Format prompt with context
        full_prompt = f"Context:\n{context}\n\nQuestion: {prompt}\nAnswer:"
        try:
            response = ollama.chat(
                model=self.model_name, 
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response['message']['content']
        except Exception as e:
            logging.error(f"LLM error: {e}")
            return "Sorry, I couldn't process your question."