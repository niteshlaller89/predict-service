import json

from fastapi import APIRouter, HTTPException

from app.models.prediction import HealthResponse, MachineLearningDataInput
from app.services.predict import TPredictService
from app.utils.config import settings
from app.utils.types import DataInput

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health(service: TPredictService) -> HealthResponse:
    is_health = False
    try:
        test_input = MachineLearningDataInput(
            **json.loads(open(settings.INPUT_EXAMPLE, "r").read())
        )
        test_point: DataInput = test_input.get_np_array()
        service.predict(test_point)
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")
