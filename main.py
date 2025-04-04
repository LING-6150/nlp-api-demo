import sys
import os
import logging
from typing import List
from fastapi import FastAPI, Query, Body
import redis
from utils import fake_nlp_prediction

# 日志目录（如果不存在就创建）
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("nlp-api")

# 强制将当前目录加入系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

# 连接 Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/predict/")
def predict_topic(text: str = Query(..., description="论文摘要内容")):
    logger.info(f"📥 收到请求文本: {text}")
    cache_key = f"prediction:{text}"
    if r.exists(cache_key):
        result = r.get(cache_key)
        logger.info("✅ 命中缓存（Redis）")
        return {"topic": result, "source": "redis_cache"}
    result = fake_nlp_prediction(text)
    logger.info(f"🧠 模型推理结果: {result}")
    r.setex(cache_key, 3600, result)
    return {"topic": result, "source": "model_inference"}

@app.post("/batch_predict/")
def batch_predict(texts: List[str] = Body(..., description="论文摘要列表")):
    results = []
    for text in texts:
        logger.info(f"📥 收到批量请求文本: {text}")
        cache_key = f"prediction:{text}"
        if r.exists(cache_key):
            result = r.get(cache_key)
            logger.info("✅ 命中缓存（Redis）")
            source = "redis_cache"
        else:
            result = fake_nlp_prediction(text)
            logger.info(f"🧠 模型推理结果: {result}")
            r.setex(cache_key, 3600, result)
            source = "model_inference"
        results.append({"text": text, "topic": result, "source": source})
    return results
