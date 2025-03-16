from fastapi import APIRouter

from oracle.schemas.prediction import PredictionCreate, PredictionPublic
from oracle.services.predictor import predict_life_expectancy

router = APIRouter(prefix="/api/v1/predictions", tags=["Predictions"])


@router.post("")
def make_prediction(prediction: PredictionCreate) -> PredictionPublic:
    return PredictionPublic(life_expectancy=predict_life_expectancy(prediction), date_of_birth=prediction.date_of_birth)
