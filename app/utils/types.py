from typing import Any, Callable

import joblib
import numpy.typing as npt

DataInput = npt.NDArray[Any]


class ModelLoadWrapper:
    JOBLIB: tuple[Callable[..., Any], str] = (joblib.load, "predict")  # type: ignore
