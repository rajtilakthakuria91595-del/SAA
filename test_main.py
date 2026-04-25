import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_positive_sentiment():
    response = client.post("/api/v1/analyze", json={"text": "FastAPI is absolutely amazing!"})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"
    assert "score" in data

def test_analyze_negative_sentiment():
    response = client.post("/api/v1/analyze", json={"text": "This is terrible and I hate it."})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "negative"
    assert "score" in data

def test_analyze_neutral_sentiment():
    response = client.post("/api/v1/analyze", json={"text": "I am eating bread."})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "neutral"

def test_analyze_validation_empty_string():
    response = client.post("/api/v1/analyze", json={"text": "   "})
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["type"] == "value_error"
