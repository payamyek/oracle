from datetime import date
from typing import List

import pandas as pd

from oracle.models.prediction import PredictionCreate, PredictionMedicalBillOfMaterial, PredictionPublic

# can't estimate beyond this age
AGE_UPPER_BOUND = 110

LIFE_TABLE = {
    "M": pd.read_pickle("data/canada_male_life_table.pkl"),
    "F": pd.read_pickle("data/canada_male_life_table.pkl"),
}

SMOKING_IMPACT_IN_MINUTES = {"M": -17, "F": -22}


def _smoking_impact(prediction: PredictionCreate) -> float:
    if prediction.smoking_daily_frequency is None:
        return 0

    days = 0

    if prediction.smoking_start_date is not None and prediction.smoking_end_date is not None:
        days = (prediction.smoking_end_date - prediction.smoking_start_date).days
    elif prediction.smoking_start_date is not None:
        days = (date.today() - prediction.smoking_start_date).days
    return (SMOKING_IMPACT_IN_MINUTES[prediction.sex] * days * prediction.smoking_daily_frequency) / (365 * 60 * 24)


def predict_life_expectancy(prediction: PredictionCreate) -> PredictionPublic:
    if prediction.age > AGE_UPPER_BOUND:
        return PredictionPublic(life_expectancy=prediction.age, date_of_birth=prediction.date_of_birth)

    expected_remaining_years = LIFE_TABLE[prediction.sex].query("age == @prediction.age")["e_x"].item()
    life_expectancy = prediction.age + expected_remaining_years + _smoking_impact(prediction)

    medical_bill_of_materials: List[PredictionMedicalBillOfMaterial] = [
        PredictionMedicalBillOfMaterial(factor="BASE_LIFE_EXPECTANCY", impact=life_expectancy),
        PredictionMedicalBillOfMaterial(factor="SMOKING", impact=_smoking_impact(prediction)),
    ]

    return PredictionPublic(
        life_expectancy=round(life_expectancy, 2),
        date_of_birth=prediction.date_of_birth,
        medical_bill_of_materials=medical_bill_of_materials,
    )
