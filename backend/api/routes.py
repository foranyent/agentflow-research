from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.orchestrator import run_research

router = APIRouter()

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    query: str
    report: str

@router.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    try:
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        print(f"[API] Received research request: {request.query}")
        result = run_research(request.query)
        
        return ResearchResponse(
            query=result["query"],
            report=result["report"]
        )
    
    except Exception as e:
        print(f"[API] Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))