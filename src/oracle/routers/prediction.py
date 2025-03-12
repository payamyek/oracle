from fastapi import APIRouter

from oracle.predictor import predict_life_expectancy
from oracle.schemas.prediction import Prediction, PredictionResponse

router = APIRouter(
    prefix="/api/v1/predictions",
    responses={404: {"description": "Not found"}},
)


@router.post("")
def make_prediction(prediction: Prediction) -> PredictionResponse:
    return PredictionResponse(
        life_expectancy=predict_life_expectancy(prediction), date_of_birth=prediction.date_of_birth
    )
