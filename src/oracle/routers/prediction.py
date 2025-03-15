from fastapi import APIRouter

from oracle.schemas.prediction import Prediction, PredictionResponse
from oracle.services.predictor import predict_life_expectancy

router = APIRouter(
    prefix="/api/v1/predictions",
)


@router.post("")
def make_prediction(prediction: Prediction) -> PredictionResponse:
    return PredictionResponse(
        life_expectancy=predict_life_expectancy(prediction), date_of_birth=prediction.date_of_birth
    )
