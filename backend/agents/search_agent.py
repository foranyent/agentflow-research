from tavily import TavilyClient
from core.config import settings

client = TavilyClient(api_key=settings.tavily_api_key)

def search(query: str) -> str:
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )
    
    results = []
    for r in response.get("results", []):
        results.append(f"Title: {r['title']}\nURL: {r['url']}\nSummary: {r['content']}\n")
    
    return "\n---\n".join(results) if results else "No results found."