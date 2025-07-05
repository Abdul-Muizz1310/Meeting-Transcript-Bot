
# FastAPI Chatbot with LangChain, OpenAI, Langfuse, and Astra DB

## Features
- Upload transcripts with metadata extraction (topic & date)
- Store and retrieve data from Astra DB (with built-in embeddings)
- Smart intent routing for summarization or question answering
- Langfuse integration for tracing

## Setup
1. Copy `.env` and fill in credentials.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `uvicorn app.main:app --reload`

## Endpoints
- `POST /upload_transcript` → Upload a transcript and auto-store
- `POST /query` → Ask questions or get summaries
