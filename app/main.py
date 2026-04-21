import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.services import analyze_text

app = FastAPI(
    title="Sentiment Analysis API",
    description="A production-ready API for analyzing text sentiment.",
    version="1.0.0"
)

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    """
    Analyzes the sentiment of the provided text.
    Returns whether the text is positive, negative, or neutral, along with a polarity score.
    """
    return analyze_text(request.text)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
