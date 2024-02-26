from fastapi import APIRouter, HTTPException

from app.models.health import HealthResponse
from app.services.predict import TPredictService

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health(service: TPredictService) -> HealthResponse:
    is_health = False
    try:
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")
