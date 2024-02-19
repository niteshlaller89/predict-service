from fastapi import APIRouter

from app.api.v1 import predictor

router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
