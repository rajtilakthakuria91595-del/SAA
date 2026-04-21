from textblob import TextBlob
from app.schemas import AnalyzeResponse

def analyze_text(text: str) -> AnalyzeResponse:
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    
    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
        
    return AnalyzeResponse(
        sentiment=sentiment,
        score=score
    )
