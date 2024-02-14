import os
from typing import Any

import joblib
from loguru import logger
from utils.errors import ModelLoadException, PredictException
from utils.types import DataInput, ModelLoadWrapperType, ModelPredictorMethod

from app.utils.config import settings


class MachineLearningModelHandlerScore(object):
    model = None
    modelLoadWrapper: dict[ModelLoadWrapperType, Any] = {
        ModelLoadWrapperType.JOBLIB: joblib.load,
    }

    @classmethod
    def predict(
        cls,
        input: DataInput,
        load_wrapper_type: ModelLoadWrapperType = ModelLoadWrapperType.JOBLIB,
        predict_method: ModelPredictorMethod = ModelPredictorMethod.PREDICT,
    ):
        model = cls.get_model(load_wrapper_type)
        if hasattr(model, predict_method):
            return getattr(model, predict_method)(input)
        raise PredictException(f"'{predict_method}' attribute is missing")

    @classmethod
    def get_model(cls, load_wrapper_type: ModelLoadWrapperType = ModelLoadWrapperType.JOBLIB):
        if cls.model is None and load_wrapper_type in ModelLoadWrapperType:
            load_wrapper_method = cls.modelLoadWrapper[load_wrapper_type]
            cls.model = cls.load(load_wrapper_method)
        return cls.model

    @staticmethod
    def load(load_wrapper_method: Any):
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
