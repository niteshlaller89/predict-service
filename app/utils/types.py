from typing import Any, Callable

import joblib  # type: ignore
import numpy.typing as npt

DataInput = npt.NDArray[Any]


class ModelLoadWrapper:
    CUSTOM: tuple[Callable[..., Any], str] = (joblib.load, "predict")  # type: ignore
    # ModelLoadWrapperType.AZURE:  tuple[Callable[..., Any], str] = ()
