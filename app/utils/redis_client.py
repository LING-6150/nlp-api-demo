import redis
import json
import logging
from app.config import REDIS_HOST, REDIS_PORT

logger = logging.getLogger("redis_client")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_from_cache(key: str):
    try:
        cached = r.get(key)
        return json.loads(cached) if cached else None
    except redis.RedisError as e:
        logger.error(f"从 Redis 获取缓存失败, key: {key}, 错误: {e}")
        return None
    except Exception as e:
        logger.error(f"解析 Redis 缓存失败, key: {key}, 错误: {e}")
        return None

def save_to_cache(key: str, value: dict, expire_seconds: int = 3600):
    try:
        r.setex(key, expire_seconds, json.dumps(value))
    except redis.RedisError as e:
        logger.error(f"保存缓存到 Redis 失败, key: {key}, 错误: {e}")

