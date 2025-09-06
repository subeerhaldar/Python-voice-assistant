# Voice Assistant QA

A standalone, voice-driven question-answering assistant using only free, open-source libraries.

## Setup

1. **Clone the repository**  
   `git clone ...`

2. **Install dependencies**  
   `pip install -r requirements.txt`

3. **Install Ollama and pull a model**  
   - [Install Ollama](https://ollama.com/download)
   - Pull a model (e.g., llama3):  
     `ollama pull llama3`
      `ollama run llama3`

4. **Configure environment variables**  
   Copy `.env.template` to `.env` and set `OLLAMA_MODEL_NAME` (e.g., `llama3`).

5. **Add documents**  
   Place `.txt` or `.md` files in `voice_qa/data/docs/` to be indexed.

6. **Run the app**  
   `cd voice_qa`
   `python -m main`

## .env template

```env
# .env.template
OLLAMA_MODEL_NAME=llama3
OLLAMA_BASE_URL=http://localhost:11434
```

## Indexing new docs

Add your `.txt` or `.md` files to `voice_qa/data/docs/` and restart the app.

## Notes

- All components are free and open-source.
- Once the LLM is downloaded, the stack runs offline.