from textblob import TextBlob
from app.schemas import AnalyzeResponse

def analyze_text(text: str) -> AnalyzeResponse:
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    
    if score > 0:
        sentiment = "positive"
        emotion = "joy" if score > 0.5 else "content"
    elif score < 0:
        sentiment = "negative"
        emotion = "anger" if score < -0.5 else "sadness"
    else:
        sentiment = "neutral"
        emotion = "neutral"
        
    return AnalyzeResponse(
        sentiment=sentiment,
        score=score,
        emotion=emotion
    )
