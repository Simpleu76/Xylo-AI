from fastapi import APIRouter
from pydantic import BaseModel
from ..tts import tts

router = APIRouter(prefix="/tts", tags=["TTS"])

class TTSRequest(BaseModel):
    text: str

@router.post("/")
async def synthesize(request: TTSRequest):
    """
    Wandelt Text in Sprache um und gibt WAV-Audio zurück.
    """
    audio_bytes = await tts.synthesize(request.text)
    return {
        "audio_base64": audio_bytes.hex()  # später ersetzen wir das durch echten Audio-Stream
    }
