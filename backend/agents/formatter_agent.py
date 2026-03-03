import anthropic
from core.config import settings

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

def format_response(query: str, summary: str) -> dict:
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""You are a research report formatter. Given the following summary for the query: "{query}"

Format this into a clean, professional research report with the following sections:
- Key Findings (3-5 bullet points)
- Detailed Analysis (2-3 paragraphs)
- Sources & Confidence (brief note on source quality)

Summary to format:
{summary}

Respond in plain text, no markdown."""
            }
        ]
    )

    return {
        "query": query,
        "report": message.content[0].text
    }