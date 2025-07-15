# 🧠 Meeting Transcript Assistant

A FastAPI-based AI backend for managing meeting transcripts — enabling users to upload transcripts, query or summarize them with natural language, and retrieve intelligent responses using OpenAI, LangChain, Langfuse, and Astra DB.

---

## 📘 Overview

This project is built to:
- 📝 Store full meeting transcripts.
- 🤖 Classify user queries as either summarization or question answering.
- 📡 Retrieve relevant past meetings using metadata and vector similarity.
- 🧠 Use LLMs (GPT-4o-mini) to answer or summarize with contextual precision.
- 🔎 Observe and manage prompts using Langfuse.

---

## How It Works

```mermaid
flowchart TD
    A(User: Frontend / CLI)

    %% Upload Transcript Path
    A -->|Submit Transcript| B[POST /upload_transcript]
    B -->|Extract Metadata| C[Metadata Extractor]
    B -->|Trace Upload| E[Langfuse Tracer]
    C -->|Store Vectors| D[Astra DB Vector Store]
    

    %% Query Path
    A -->|Submit Query| F[POST /query]
    F -->|Classify Intent| G[Intent Classifier]
    G -->|Determine Flow| H[Routing Decision]

    H -->|Generate Summary| I[Summarizer Chain]
    H -->|Answer Questions| J[QA Chain]
    F -->|Extract Metadata| K[Metadata Extractor]
    K -->|Retrive Vectors| L[Astra DB Vector Store]
    L-->|Context| H[Routing Decision]

    F -->|Trace Query| E
```

---

## 📂 Project Structure

```
📁 app/
├── chains/
│   ├── intent_classifier.py     # Detects intent + extracts topic/date
│   ├── metadata_extractor.py    # Extracts metadata from transcripts
│   ├── qa_chain.py              # Answers questions using relevant docs
│   └── summarizer_chain.py      # Summarizes documents based on query
├── astra_store.py               # Astra DB vector storage logic
├── langfuse.py                  # Langfuse prompt integration + tracing
├── routes.py                    # FastAPI API routes
main.py                          # App entry point
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/meeting-transcript-assistant.git
cd meeting-transcript-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the root directory with:

```dotenv
OPENAI_API_KEY=your_openai_api_key

ASTRA_DB_ID=your_astra_db_id
ASTRA_DB_KEY=your_astra_db_key
ASTRA_DB_TABLE=meeting_transcripts
ASTRA_DB_API_ENDPOINT=https://your-db-id-region.apps.astra.datastax.com

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

### 4. Run the Prompts.py

```bash
cd prompts
python prompts.py
```

### 5. Run the Application

```bash
uvicorn main:app --reload
```

> API docs will be available at [http://localhost:8000/docs](http://localhost:8000/docs)


---

## 📡 API Endpoints

### 🔹 POST `/upload_transcript`

**Request:**
```json
{
  "transcript": "Today we discussed updates for the Q3 marketing roadmap..."
}
```

**Response:**
```json
{
  "status": "stored",
  "metadata": {
    "topic": "q3 marketing",
    "date": "2025-07-13"
  }
}
```

---

### 🔹 POST `/query`

**Request:**
```json
{
  "query": "Can you summarize the meeting about Q3 marketing?"
}
```

**Response:**
```json
{
  "intent": "summarization",
  "result": "The meeting focused on Q3 product strategy, emphasizing customer outreach..."
}
```

---

## 🧠 Chain Breakdown

### ✳️ `intent_classifier.py`
- `detect_intent()`: Determines if the query is a question or summarization.
- `extract_topic_date()`: Extracts metadata fields from a natural language question.

### 🏷️ `metadata_extractor.py`
- `extract_metadata()`: Extracts structured fields like topic/date from raw transcripts. Ensures JSON parsing and handles errors.

### ❓ `qa_chain.py`
- `run_qa_chain()`: Answers user questions based on semantic search + context.

### 📝 `summarizer_chain.py`
- `run_summarizer()`: Generates concise summaries for transcripts based on context and intent.

---

## 📈 Observability with Langfuse

Langfuse is used to:
- Manage prompt templates (`detect_intent`, `extract_metadata`, `qa`, `summarizer`)
- Trace LLM calls and visualize latency, tokens, etc.
- Inject `CallbackHandler` for automatic logging.
