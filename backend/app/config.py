import os
from dotenv import load_dotenv

# .env Datei laden (falls vorhanden)
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Xylo AI"
    VERSION: str = "1.0.0"

    # Backend
    SECRET_KEY: str = os.getenv("XYLO_SECRET_KEY", "changeme")
    ADMIN_PASSWORD: str = os.getenv("XYLO_ADMIN_PASSWORD", "admin123")

    # Ollama
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    # TTS (Piper)
    PIPER_HOST: str = os.getenv("PIPER_HOST", "localhost")
    PIPER_PORT: int = int(os.getenv("PIPER_PORT", 10200))
    PIPER_VOICE: str = os.getenv("PIPER_VOICE", "en_US-libritts-high")

    # Websuche
    USER_AGENT: str = os.getenv("XYLO_USER_AGENT", "XyloAI/1.0")

settings = Settings()
