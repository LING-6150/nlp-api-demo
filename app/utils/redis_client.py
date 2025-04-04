import redis
import json
import logging
import os

logger = logging.getLogger("redis_client")

# Render 上用的是完整 Redis URL
REDIS_URL = os.getenv("REDIS_URL")
USE_REDIS = REDIS_URL is not None  # 只要设置了 URL，就启用 Redis

# 初始化 Redis 客户端
r = redis.from_url(REDIS_URL, decode_responses=True) if USE_REDIS else None

def get_from_cache(key: str):
    if not r:
        return None
    try:
        cached = r.get(key)
        return json.loads(cached) if cached else None
    except redis.RedisError as e:
        logger.error(f"从 Redis 获取缓存失败, key: {key}, 错误: {e}")
        return None

def save_to_cache(key: str, value: dict, expire_seconds: int = 3600):
    if not r:
        return
    try:
        r.setex(key, expire_seconds, json.dumps(value))
    except redis.RedisError as e:
        logger.error(f"保存缓存到 Redis 失败, key: {key}, 错误: {e}")
