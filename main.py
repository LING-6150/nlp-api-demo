import sys
import os

# 强制将当前目录加入系统路径（关键）
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Query
import redis
from utils import fake_nlp_prediction

app = FastAPI()

# 连接 Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/predict/")
def predict_topic(text: str = Query(..., description="论文摘要内容")):
    cache_key = f"prediction:{text}"
    
    # 如果有缓存
    if r.exists(cache_key):
        return {"topic": r.get(cache_key), "source": "redis_cache"}
    
    # 如果没有缓存
    result = fake_nlp_prediction(text)
    r.setex(cache_key, 3600, result)
    return {"topic": result, "source": "model_inference"}
