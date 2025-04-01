from datetime import date
from oracle.models.prediction import PredictionComponent, PredictionCreate


SMOKING_IMPACT_IN_MINUTES = {"M": -17, "F": -22}


def smoking_component(prediction: PredictionCreate) -> PredictionComponent:
    adjustment = 0

    if prediction.smoking_daily_frequency is not None:
        days_smoked = 0

        if prediction.smoking_start_date is not None and prediction.smoking_end_date is not None:
            days_smoked = (prediction.smoking_end_date - prediction.smoking_start_date).days
        elif prediction.smoking_start_date is not None:
            days_smoked = (date.today() - prediction.smoking_start_date).days

        adjustment = (SMOKING_IMPACT_IN_MINUTES[prediction.sex] * days_smoked * prediction.smoking_daily_frequency) / (
            365 * 60 * 24
        )

    return PredictionComponent(type="SMOKING", adjustment=adjustment)
