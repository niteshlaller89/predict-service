from enum import Enum
from typing import Any

import numpy.typing as npt

DataInput = npt.NDArray[Any]


class ModelLoadWrapperType(Enum):
    JOBLIB = "joblib.load"


class ModelPredictorMethod(str, Enum):
    PREDICT = "predict"
