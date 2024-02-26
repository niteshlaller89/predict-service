from fastapi import APIRouter, Body, File, HTTPException, UploadFile

from app.models.v1.predict import PredictionInput, PredictionResponse
from app.services.predict import TPredictService

router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
    name="predict:get-data",
    summary="Generate a prediction from data point using specific ml model",
)
async def predict(
    p_service: TPredictService,
    data: PredictionInput = Body(),
    file: UploadFile = File(description="input file contains data"),
) -> PredictionResponse:
    if not file or not data:
        raise HTTPException(status_code=404, detail="argument invalid!")
    try:
        prediction = p_service.predict(input)

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return MachineLearningResponse(prediction=prediction)
