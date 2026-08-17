from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_car_price

router = APIRouter()

class CarFeatures(BaseModel):
    year: float
    km_driven: float
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    seats: float



@router.post('/predict')
def predict_price(car: CarFeatures, user = Depends(get_current_user), _= Depends(get_api_key)):
    prediction = predict_car_price(car.model_dump()) # converts to python dict
    return {'predicted_price': prediction}