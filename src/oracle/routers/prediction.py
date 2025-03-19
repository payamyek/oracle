from fastapi import APIRouter

from oracle.dependencies import CommonHeaders, SessionDep, VerifyApiKeyDep
from oracle.models.prediction import PredictionCreate, PredictionPublic
from oracle.services.predictor import predict_life_expectancy

router = APIRouter(prefix="/api/v1/predictions", tags=["Predictions"])


@router.post("", dependencies=[VerifyApiKeyDep])
def make_prediction(prediction: PredictionCreate, headers: CommonHeaders, session: SessionDep) -> PredictionPublic:
    return PredictionPublic(life_expectancy=predict_life_expectancy(prediction), date_of_birth=prediction.date_of_birth)
