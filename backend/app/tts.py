import aiohttp
from fastapi import HTTPException
from .config import settings

class TTSClient:
    def __init__(self):
        self.host = settings.PIPER_HOST
        self.port = settings.PIPER_PORT
        self.voice = settings.PIPER_VOICE

    async def synthesize(self, text: str) -> bytes:
        """
        Sendet Text an Piper TTS und gibt Audio (WAV) zurück.
        """
        url = f"http://{self.host}:{self.port}/synthesize"

        payload = {
            "text": text,
            "voice": self.voice
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Piper TTS Fehler: {await response.text()}"
                    )

                return await response.read()  # Audio als Bytes

tts = TTSClient()
