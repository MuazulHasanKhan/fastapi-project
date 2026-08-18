import json
import redis
from app.core.config import settings
import os
from dotenv import load_dotenv
# redis_client = redis.Redis.from_url(settings.REDIS_URL)

# two functions assuming that similar query was asked earlier

REDIS_URL = os.getenv('REDIS_URL')

redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)

def get_cached_pediction(key:str):
    value = redis_client.get(key)

    if value:
        return json.loads(value)
    return None

def set_cached_prediction(key:str, value:dict, expiry: int ):
    redis_client.setex(key, expiry, json.dumps(value))
