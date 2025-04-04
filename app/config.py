import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_EXPIRE_SECONDS = 3600
USE_REDIS = os.getenv("USE_REDIS", "true").lower() == "true"
