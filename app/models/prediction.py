from typing import Any

import numpy as np
import numpy.typing as npt
from pydantic import BaseModel


class MachineLearningResponse(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: bool


class MachineLearningDataInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

    def get_np_array(self) -> npt.NDArray[Any]:
        return np.array(
            [
                [
                    self.feature1,
                    self.feature2,
                    self.feature3,
                ]
            ]
        )
