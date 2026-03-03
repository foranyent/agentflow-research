# AgentFlow Research Assistant

A multi-agent AI research system that takes a user query and returns a structured research report in seconds.

## How It Works

A coordinated pipeline of 4 specialized agents:

1. **Orchestrator Agent** — breaks the query into focused search strategies
2. **Search Agent** — retrieves real-time web results via Tavily
3. **Summarizer Agent** — condenses findings using Claude
4. **Formatter Agent** — structures everything into a clean research report

## Tech Stack

- **Backend:** FastAPI, Python
- **AI:** Anthropic Claude (claude-sonnet)
- **Search:** Tavily API
- **Frontend:** Streamlit
- **Deployment:** Render (backend), Streamlit Cloud (frontend)

## Running Locally

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
   pip install -r backend/requirements.txt
```
3. Create a `.env` file in the root with your API keys:
```
   ANTHROPIC_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
```
4. Start the backend:
```bash
   python run.py
```
5. In a second terminal, start the frontend:
```bash
   streamlit run frontend/app.py
```
6. Open your browser at `http://localhost:8501`

## API Endpoint

`POST /api/v1/research`

Request:
```json
{
  "query": "Your research question here"
}
```

Response:
```json
{
  "query": "Your research question here",
  "report": "Structured research report..."
}
```

## Architecture
```
User Query (Streamlit)
    → FastAPI /research endpoint
        → Orchestrator Agent (Claude)
            → Search Agent (Tavily)
            → Summarizer Agent (Claude)
            → Formatter Agent (Claude)
    → Structured Report → UI
```