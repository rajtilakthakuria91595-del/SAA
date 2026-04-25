import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.services import analyze_text

from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Sentiment Analysis API",
    description="A production-ready API for analyzing text sentiment.",
    version="1.0.0"
)




@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    """
    Analyzes the sentiment of the provided text.
    Returns whether the text is positive, negative, or neutral, along with a polarity score.
    """
    return analyze_text(request.text)

# Serve the frontend UI at the root
frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
if os.path.isdir(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

if __name__ == "__main__":
    # Fetch the port Render assigns, or default to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    
    # Removed reload=True for production stability
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
