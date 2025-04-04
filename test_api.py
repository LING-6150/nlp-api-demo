from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_single():
    response = client.get("/predict/", params={"text": "This study uses AI to detect patterns in data."})
    assert response.status_code == 200
    data = response.json()
    assert "topic" in data
    assert "confidence" in data
    assert "source" in data
    assert data["confidence"] >= 0.7

def test_batch_predict():
    texts = [
        "This study uses AI to detect patterns in data.",
        "We use CRISPR for rice engineering.",
        "Climate change impacts are analyzed."
    ]
    response = client.post("/batch_predict/", json=texts)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    for item in data:
        assert "topic" in item
        assert "confidence" in item
        assert "source" in item
        assert "text" in item

