from fastapi import APIRouter

from oracle.dependencies import VerifyApiKeyDep
from oracle.models.prediction import PredictionCreate, PredictionPublic
from oracle.services.predictor.predictor import predict_life_expectancy

router = APIRouter(prefix="/api/v1/predictions", tags=["Predictions"])


@router.post("", dependencies=[VerifyApiKeyDep])
def make_prediction(
    prediction: PredictionCreate,
) -> PredictionPublic:
    return predict_life_expectancy(prediction)
