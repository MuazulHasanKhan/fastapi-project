import json
import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)

# two functions assuming that similar query was asked earlier


def get_cached_pediction(key:str):
    value = redis_client.get(key)

    if value:
        return json.loads(value)
    return None

def set_cached_prediction(key:str, value:dict, expiry: int ):
    redis_client.setex(key, expiry, json.dums(value))
