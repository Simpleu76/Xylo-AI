from fastapi import APIRouter
from pydantic import BaseModel
from ..search import search

router = APIRouter(prefix="/search", tags=["Search"])

class SearchRequest(BaseModel):
    query: str
    max_results: int = 5

@router.post("/")
def web_search(request: SearchRequest):
    """
    Führt eine Websuche aus und gibt die besten Ergebnisse zurück.
    """
    results = search.search(request.query, request.max_results)
    return {"results": results}
