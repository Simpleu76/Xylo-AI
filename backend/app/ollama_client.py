import aiohttp
from fastapi import HTTPException
from .config import settings

class OllamaClient:
    def __init__(self):
        self.base_url = settings.OLLAMA_HOST

    async def generate(self, prompt: str, model: str = "llama3"):
        """
        Sendet eine Anfrage an Ollama und gibt die Antwort zurück.
        """
        url = f"{self.base_url}/api/generate"

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Ollama Fehler: {await response.text()}"
                    )
                data = await response.json()
                return data.get("response", "")

    async def stream(self, prompt: str, model: str = "llama3"):
        """
        Streamt die Antwort von Ollama (Token für Token).
        """
        url = f"{self.base_url}/api/generate"

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": True
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Ollama Fehler: {await response.text()}"
                    )

                async for line in response.content:
                    try:
                        chunk = line.decode("utf-8").strip()
                        if chunk:
                            yield chunk
                    except Exception:
                        continue


ollama = OllamaClient()
