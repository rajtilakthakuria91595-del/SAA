from pydantic import BaseModel, field_validator
from typing import Literal, Optional

class AnalyzeRequest(BaseModel):
    text: str

    @field_validator('text')
    def text_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Text cannot be empty or strictly whitespace')
        return v

class AnalyzeResponse(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral']
    score: float
    emotion: Optional[str] = None
