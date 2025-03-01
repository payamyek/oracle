from fastapi import APIRouter

from oracle.model import predict_life_expectancy
from oracle.schemas.predictions import Prediction, PredictionResponse

router = APIRouter(
    prefix="/predictions",
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def make_prediction(prediction: Prediction) -> PredictionResponse:
    return PredictionResponse(life_expectancy=predict_life_expectancy(prediction.age, prediction.sex))
