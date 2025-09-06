import os
import sys
from dotenv import load_dotenv
import speech_io
import retriever
import llm_client

def main():
    load_dotenv()
    model_name = os.getenv("OLLAMA_MODEL_NAME", "llama3")
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    retr = retriever.Retriever()
    llm = llm_client.LLMClient(model_name, ollama_url)

    print("Voice Assistant QA (say 'exit' to quit)")
    try:
        while True:
            print("\nListening...")
            speech_io.speak("I am listening Boss. Please speak.")
            user_text = speech_io.listen_and_transcribe()
            if not user_text:
                continue
            print(f"You said: {user_text}")
            if user_text.strip().lower() == "exit":
                print("Goodbye!")
                break

            docs = retr.search(user_text)
            context = "\n".join([d.page_content for d in docs])
            response = llm.ask(user_text, context)
            print(f"Assistant: {response}")
            speech_io.speak(response)
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()