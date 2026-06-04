from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Router importieren
from .routers.chat import router as chat_router
from .routers.tts import router as tts_router
from .routers.search import router as search_router

app = FastAPI(
    title="Xylo AI Backend",
    version="1.0.0",
    description="Backend API für den KI-Assistenten Xylo"
)

# CORS erlauben (Frontend → Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router registrieren
app.include_router(chat_router)
app.include_router(tts_router)
app.include_router(search_router)

@app.get("/")
def root():
    return {"message": "Xylo Backend läuft!"}
