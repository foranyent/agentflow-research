import anthropic
from core.config import settings
from agents.search_agent import search
from agents.summarizer_agent import summarize
from agents.formatter_agent import format_response

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

def run_research(query: str) -> dict:
    print(f"[Orchestrator] Received query: {query}")

    # Step 1 — Orchestrator decides search strategy
    planning_message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": f"""You are a research orchestrator. A user wants to research: "{query}"

Your job is to produce 2-3 focused search queries that will gather the best information on this topic.
Respond with only the search queries, one per line, nothing else."""
            }
        ]
    )

    search_queries = planning_message.content[0].text.strip().split("\n")
    search_queries = [q.strip() for q in search_queries if q.strip()]
    print(f"[Orchestrator] Search queries planned: {search_queries}")

    # Step 2 — Search agent runs each query
    all_results = []
    for q in search_queries:
        print(f"[Search Agent] Searching: {q}")
        results = search(q)
        all_results.append(results)

    combined_results = "\n\n===\n\n".join(all_results)

    # Step 3 — Summarizer agent condenses results
    print("[Summarizer Agent] Summarizing results...")
    summary = summarize(query, combined_results)

    # Step 4 — Formatter agent produces final report
    print("[Formatter Agent] Formatting report...")
    final_report = format_response(query, summary)

    return final_report