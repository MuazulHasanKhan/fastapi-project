import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cached_prediction, get_cached_pediction

model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data: dict):
    cache_key =  " ".join([str(val) for val in data.values()])
    cache = get_cached_pediction(cache_key)

    if cache:
        return cache

    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cached_prediction(cache_key, prediction)
    return prediction

