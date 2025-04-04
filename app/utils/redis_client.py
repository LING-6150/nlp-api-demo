# app/utils/redis_client.py

import os
import redis
import json
import logging

logger = logging.getLogger("redis_client")

# 从环境变量读取 Redis 连接信息
REDIS_URL = os.getenv("REDIS_URL")
USE_REDIS = os.getenv("USE_REDIS", "false").lower() == "true"

# 初始化 Redis 客户端（如果启用）
if USE_REDIS and REDIS_URL:
    r = redis.from_url(REDIS_URL, decode_responses=True)
    logger.info("✅ Redis client connected using REDIS_URL.")
else:
    r = None
    logger.warning("⚠️ Redis is disabled or REDIS_URL not found.")

def get_from_cache(key: str):
    if not r:
        return None
    try:
        cached = r.get(key)
        return json.loads(cached) if cached else None
    except redis.RedisError as e:
        logger.error(f"❌ 从 Redis 获取缓存失败, key: {key}, 错误: {e}")
        return None

def save_to_cache(key: str, value: dict, expire_seconds: int = 3600):
    if not r:
        return
    try:
        r.setex(key, expire_seconds, json.dumps(value))
    except redis.RedisError as e:
        logger.error(f"❌ 保存缓存到 Redis 失败, key: {key}, 错误: {e}")
