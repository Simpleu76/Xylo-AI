# Xylo‑AI  
Ein modularer KI‑Assistent mit FastAPI, Ollama, Piper TTS und DuckDuckGo‑Suche.

Xylo‑AI ist ein leichtgewichtiges, dockerisiertes Backend für einen persönlichen KI‑Assistenten.  
Es kombiniert lokale KI‑Modelle (Ollama), Text‑zu‑Sprache (Piper), Websuche und modulare Router in einer klaren API‑Struktur.

---

## 🚀 Features

- **Chat‑API**  
  KI‑Antworten über Ollama (lokale LLMs wie Llama 3, Mistral, Phi usw.)

- **TTS‑API**  
  Text‑zu‑Sprache über Piper (schnell, offline, deutschfähig)

- **Websuche**  
  DuckDuckGo‑basierte Suche mit sauberem JSON‑Output

- **FastAPI Backend**  
  Moderne, schnelle API mit automatischer Dokumentation

- **Docker‑Support**  
  Komplett containerisiert, sofort startklar

---

## 📂 Projektstruktur

backend/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── ollama_client.py
│   ├── search.py
│   ├── tts.py
│   └── routers/
│       ├── chat.py
│       ├── search.py
│       └── tts.py
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

Code

---

## 🛠 Installation & Start

### 1. Repository klonen

```bash
git clone https://github.com/Simpleu76/Xylo-AI.git
cd Xylo-AI
2. Docker starten
bash
docker-compose up --build
3. API öffnen
Health‑Check:
http://localhost:8000

API‑Dokumentation (Swagger):
http://localhost:8000/docs

🧠 API‑Endpoints
POST /chat/
Generiert KI‑Antworten.

Body:

json
{
  "prompt": "Hallo",
  "model": "llama3"
}
POST /tts/
Gibt Audio (Hex/Base64) zurück.

Body:

json
{
  "text": "Hallo, ich bin Xylo."
}
POST /search/
Websuche über DuckDuckGo.

Body:

json
{
  "query": "Was ist FastAPI?",
  "max_results": 5
}
🧩 Anforderungen
Docker & Docker Compose

Ollama installiert (für lokale KI‑Modelle)

Piper installiert (für TTS)

📌 Roadmap
[ ] Websocket‑Streaming

[ ] Voice‑Streaming

[ ] Memory‑System

[ ] Agent‑Tools

[ ] Addon‑System

[ ] Frontend (React / Next.js)

[ ] Mobile‑App

📄 Lizenz
Dieses Projekt ist aktuell proprietär (privat).
Lizenz wird später ergänzt.

👤 Autor
Luca (Simpleu76)  
Xylo‑AI – persönlicher KI‑Assistent

Code

---

Wenn du willst, kann ich dir auch direkt:

- eine **.gitignore** erstellen  
- ein **Logo** für Xylo designen  
- eine **Roadmap.md** machen  
- ein **Frontend‑Starterprojekt** generieren  

Sag einfach Bescheid.
