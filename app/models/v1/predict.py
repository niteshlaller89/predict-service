import json
from enum import Enum
from typing import Annotated, Any

from pydantic import BaseModel, Field, model_validator


class PredictionResponse(BaseModel):
    data: float


class PredictionInput(BaseModel):
    modelId: Annotated[
        str, Field(min_length=1, pattern=r"^model*$", description="unique identifier of ml model")
    ]

    @model_validator(mode="before")
    @classmethod
    def validate_to_json(cls, value: dict[Any, Any]):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
