from fastapi import APIRouter

from oracle.model import predict_life_expectancy
from oracle.schemas.predictions import Prediction

router = APIRouter(
    prefix="/predictions",
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create_item(prediction: Prediction):
    return {"life_expectancy": predict_life_expectancy(prediction.age, prediction.sex)}
