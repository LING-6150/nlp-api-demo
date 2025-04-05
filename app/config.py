import os
from urllib.parse import urlparse

# 优先从 REDIS_URL 解析出 host 和 port
redis_url = os.getenv("REDIS_URL")
if redis_url:
    parsed_url = urlparse(redis_url)
    REDIS_HOST = parsed_url.hostname
    REDIS_PORT = parsed_url.port
else:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

CACHE_EXPIRE_SECONDS = 3600
USE_REDIS = bool(redis_url)
