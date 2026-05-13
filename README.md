# local-file-rag
AI powered semantic search over local documents using RAG

# status
under active deployment - day 1 of 14

# stack 
- Python 3.11
- OpenAI API (embeddings + LLM)
- ChromaDB (vector storage)
- LlamaIndex (RAG framework)
- Streamlit (UI)

# setup

```bash
git clone https://github.com/swastipahuja2002/local-file-rag.git
cd local-file-rag
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then add your OpenAI API key
```

##roadmap 
- [x] Day 1: Project setup, OpenAI hello world
- [x] Day 2: File loaders (PDF, DOCX, PPTX, TXT)
- [ ] Day 3: Text chunking
- [ ] Day 4: Embeddings + cosine similarity
- [ ] Day 5: ChromaDB integration
- [ ] Day 6: Semantic retrieval
- [ ] Day 7: End-to-end RAG
- [ ] Days 8–9: LlamaIndex refactor
- [ ] Days 10–11: Streamlit UI
- [ ] Days 12–14: Polish + showcase