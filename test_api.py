import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.redis_client import r  # 确保你正确导入 Redis 客户端

@pytest.fixture(autouse=True)
def clear_redis():
    """
    每个测试运行前后清空 Redis 缓存，确保测试环境隔离。
    """
    r.flushdb()
    yield
    r.flushdb()

@pytest.fixture(scope="module")
def client():
    """
    提供一个共享的 TestClient 实例，供所有测试使用。
    """
    with TestClient(app) as client:
        yield client

def test_predict_single(client):
    text = "This study uses AI to detect patterns in data."
    response = client.get("/predict/", params={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert "topic" in data
    assert "confidence" in data
    assert "source" in data
    assert data["confidence"] >= 0.7

def test_batch_predict(client):
    texts = [
        "This study uses AI to detect patterns in data.",
        "We use CRISPR for rice engineering.",
        "Climate change impacts are analyzed."
    ]
    response = client.post("/batch_predict/", json={"texts": texts})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == len(texts)
    for item in data:
        assert "topic" in item
        assert "confidence" in item
        assert "source" in item
        assert "text" in item

def test_cache_behavior(client):
    test_text = "Climate change is a major issue."
    response1 = client.get("/predict/", params={"text": test_text})
    response2 = client.get("/predict/", params={"text": test_text})
    assert response1.status_code == 200
    assert response2.status_code == 200
    data1 = response1.json()
    data2 = response2.json()
    assert data1["topic"] == data2["topic"]
    assert data1["confidence"] == data2["confidence"]
    assert data2["source"] == "redis_cache"

def test_predict_empty_input(client):
    response = client.get("/predict/", params={"text": ""})
    assert response.status_code == 200
    data = response.json()
    assert "topic" in data
    assert "confidence" in data
