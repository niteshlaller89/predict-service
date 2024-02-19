from fastapi import APIRouter, HTTPException

from app.models.prediction import MachineLearningDataInput, MachineLearningResponse
from app.services.predict import TPredictService
from app.utils.types import DataInput

router = APIRouter()


@router.post(
    "/predict", response_model=MachineLearningResponse, name="predict:get-data", summary=""
)
async def predict(
    data_input: MachineLearningDataInput, service: TPredictService
) -> MachineLearningResponse:

    if not data_input:
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")
    try:
        data_point: DataInput = data_input.get_np_array()

        ## Change this portion for other types of models
        ## Add the correct type hinting when completed
        prediction = service.predict(data_point)

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return MachineLearningResponse(prediction=prediction)
