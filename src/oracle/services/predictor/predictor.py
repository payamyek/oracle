from typing import List

from oracle.models.prediction import PredictionCreate, PredictionComponent, PredictionPublic
from oracle.services.predictor.life_expectancy import life_expectancy_component
from oracle.services.predictor.smoking import smoking_component


def predict_life_expectancy(prediction: PredictionCreate) -> PredictionPublic:
    components: List[PredictionComponent] = [
        life_expectancy_component(prediction),
        smoking_component(prediction),
    ]

    return PredictionPublic(
        date_of_birth=prediction.date_of_birth,
        components=components,
    )
