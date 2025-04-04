import os
import sys
import logging
import json
from typing import List
from fastapi import FastAPI, Query, Body

# 从新模块导入各部分逻辑
from app.services.predictor import predict_topic as predict_topic_logic
from app.services.logger import write_log, init_csv
from app.utils.redis_client import get_from_cache, save_to_cache
from app.config import REDIS_HOST, REDIS_PORT, CACHE_EXPIRE_SECONDS

# 确保日志目录存在
if not os.path.exists("logs"):
    os.makedirs("logs")

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("nlp-api")

app = FastAPI()

# 初始化 CSV 文件（写入表头）
init_csv()

@app.get("/predict/")
def predict(text: str = Query(..., description="论文摘要内容")):
    logger.info(f"📥 收到请求文本: {text}")
    cache_key = f"prediction:{text}"
    
    # 尝试从 Redis 缓存获取结果
    result = get_from_cache(cache_key)
    if result:
        logger.info("✅ 命中缓存（Redis）")
        write_log(text, result["topic"], result["confidence"], "redis_cache")
        result["source"] = "redis_cache"
        return result

    # 调用 predictor 模块处理业务逻辑
    result = predict_topic_logic(text)
    logger.info(f"🧠 模型推理结果: {result}")
    
    # 将结果保存到 Redis，并写入日志
    save_to_cache(cache_key, result, CACHE_EXPIRE_SECONDS)
    write_log(text, result["topic"], result["confidence"], "model_inference")
    result["source"] = "model_inference"
    return result

@app.post("/batch_predict/")
def batch_predict(texts: List[str] = Body(..., description="论文摘要列表")):
    results = []
    for text in texts:
        logger.info(f"📥 批量请求文本: {text}")
        cache_key = f"prediction:{text}"
        result = get_from_cache(cache_key)
        if result:
            logger.info("✅ 命中缓存（Redis）")
            source = "redis_cache"
        else:
            result = predict_topic_logic(text)
            logger.info(f"🧠 模型推理结果: {result}")
            save_to_cache(cache_key, result, CACHE_EXPIRE_SECONDS)
            source = "model_inference"
        write_log(text, result["topic"], result["confidence"], source)
        result["source"] = source
        result["text"] = text
        results.append(result)
    return results
