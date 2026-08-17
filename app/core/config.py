import os
from dotenv import load_dotenv

# this function will load the environment variables from the .env file  
load_dotenv()


class Settings:
    PROJECT_NAME:str = 'Car Pice API'
    API_KEY: str = os.getenv('API_KEY', 'demo-key')
    # second value is failsafe case

    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'secret')
    JWT_ALGORITHM: str = 'HS256'
    REDIS_URL: str = os.getenv('REDIS_URL', 'redis://localhost:6379')
    MODEL_PATH: str = 'app/models/model.pkl'

settings = Settings()