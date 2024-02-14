from api.v1 import predictor
from fastapi import APIRouter

router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
