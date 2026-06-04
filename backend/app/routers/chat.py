from fastapi import APIRouter
from pydantic import BaseModel
from ..ollama_client import ollama

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    prompt: str
    model: str = "llama3"

@router.post("/")
async def chat(request: ChatRequest):
    """
    Normale Chat-Antwort (kein Streaming).
    """
    response = await ollama.generate(
        prompt=request.prompt,
        model=request.model
    )
    return {"response": response}
