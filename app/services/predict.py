import os
from typing import Annotated, Any

from fastapi import Depends, File
from loguru import logger

from app.utils.config import settings
from app.utils.errors import ModelLoadException, PredictException
from app.utils.types import DataInput, ModelLoadWrapper


class PredictService:
    def __init__(self, model_loader: Any = ModelLoadWrapper.CUSTOM):
        (load_method, model_predictor_method) = model_loader
        self.model = self.load(load_method)
        if hasattr(self.model, model_predictor_method):
            self.predictor = getattr(self.model, model_predictor_method)
        else:
            raise PredictException(f"'{model_predictor_method}' attribute is missing")

    def load(self, load_wrapper_method: Any) -> Any:
        model = None
        if settings.MODEL_PATH.endswith("/"):
            path = f"{settings.MODEL_PATH}{settings.MODEL_NAME}"
        else:
            path = f"{settings.MODEL_PATH}/{settings.MODEL_NAME}"
        if not os.path.exists(path):
            message = f"Machine learning model at {path} not exists!"
            logger.error(message)
            raise FileNotFoundError(message)
        model = load_wrapper_method(path)
        if not model:
            message = f"Model {model} could not load!"
            logger.error(message)
            raise ModelLoadException(message)
        return model

    def predict(self, input: DataInput, file: File) -> Any:
        return self.predictor(input)


def get_predict_service() -> PredictService:
    return PredictService()


TPredictService = Annotated[PredictService, Depends(get_predict_service)]
