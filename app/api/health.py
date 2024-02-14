import json

from fastapi import APIRouter, HTTPException
from models.prediction import HealthResponse, MachineLearningDataInput
from services.predict import MachineLearningModelHandlerScore as model
from utils.types import DataInput

from app.utils.config import settings

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health() -> HealthResponse:
    is_health = False
    try:
        test_input = MachineLearningDataInput(
            **json.loads(open(settings.INPUT_EXAMPLE, "r").read())
        )
        test_point: DataInput = test_input.get_np_array()
        model.predict(test_point)
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")
