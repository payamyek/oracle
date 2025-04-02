import pandas as pd

from oracle.models.prediction import PredictionComponent, PredictionCreate


_AGE_UPPER_BOUND = 110

_LIFE_TABLE = {
    "M": pd.read_pickle("data/canada_male_life_table.pkl"),
    "F": pd.read_pickle("data/canada_female_life_table.pkl"),
}


def life_table_component(prediction: PredictionCreate) -> PredictionComponent:
    adjustment = prediction.age

    if prediction.age <= _AGE_UPPER_BOUND:
        expected_remaining_years = _LIFE_TABLE[prediction.sex].query("age == @prediction.age")["e_x"].item()
        adjustment = prediction.age + expected_remaining_years

    return PredictionComponent(type="LIFE_TABLE", adjustment=adjustment)
