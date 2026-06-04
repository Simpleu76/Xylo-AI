from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests

class WebSearch:
    def __init__(self):
        self.ddg = DDGS()

    def search(self, query: str, max_results: int = 5):
        """
        Führt eine DuckDuckGo-Suche aus und gibt die besten Ergebnisse zurück.
        """
        results = self.ddg.text(query, max_results=max_results)
        output = []

        for r in results:
            output.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "snippet": r.get("body")
            })

        return output

    def fetch_page_text(self, url: str) -> str:
        """
        Holt den Text einer Webseite (optional für spätere Features).
        """
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text(separator="\n")
        except Exception:
            return "Fehler beim Laden der Seite."

search = WebSearch()
