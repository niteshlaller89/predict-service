import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "predict-service"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"
    LOGGING_LEVEL: str = logging.getLevelName(logging.INFO)
    MODEL_PATH: str = "./ml/model/"
    MODEL_NAME: str = "model.pkl"
    INPUT_EXAMPLE: str = "./ml/model/examples/example.json"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
