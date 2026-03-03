import anthropic
from core.config import settings

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

def summarize(query: str, search_results: str) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""You are a research summarizer. Given the following search results for the query: "{query}"
                
Summarize the key findings in a clear, concise way. Focus on the most relevant and important information.

Search Results:
{search_results}

Provide a well-structured summary."""
            }
        ]
    )
    
    return message.content[0].text