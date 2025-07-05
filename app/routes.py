from fastapi import APIRouter
from pydantic import BaseModel
from app.chains.metadata_extractor import extract_metadata
from app.chains.intent_classifier import detect_intent, extract_topic_date
from app.chains.qa_chain import run_qa_chain
from app.chains.summarizer_chain import run_summarizer
from app.astra_store import AstraStore

router = APIRouter()
store = AstraStore()

class TranscriptRequest(BaseModel):
    transcript: str

class QueryRequest(BaseModel):
    query: str

@router.post("/upload_transcript")
async def upload_transcript(request: TranscriptRequest):
    metadata = extract_metadata(request.transcript)
    store.add_document(request.transcript, metadata)
    return {"status": "stored", "metadata": metadata}

@router.post("/query")
async def handle_query(payload: QueryRequest):
    query = payload.query
    intent = detect_intent(query)
    metadata = extract_topic_date(query)
    docs = store.query(topic=metadata.get("topic"), date=metadata.get("date"), vector_query=query)
    if intent == "summarization":
        result = run_summarizer(query, docs)
    else:
        result = run_qa_chain(query, docs)
    return {"intent": intent, "result": result.content}
