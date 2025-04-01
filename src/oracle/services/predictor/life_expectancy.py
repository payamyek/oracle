# can't estimate beyond this age
import pandas as pd

from oracle.models.prediction import PredictionComponent, PredictionCreate


AGE_UPPER_BOUND = 110

LIFE_TABLE = {
    "M": pd.read_pickle("data/canada_male_life_table.pkl"),
    "F": pd.read_pickle("data/canada_female_life_table.pkl"),
}


def life_expectancy_component(prediction: PredictionCreate) -> PredictionComponent:
    adjustment = prediction.age

    if prediction.age <= AGE_UPPER_BOUND:
        expected_remaining_years = LIFE_TABLE[prediction.sex].query("age == @prediction.age")["e_x"].item()
        adjustment = prediction.age + expected_remaining_years

    return PredictionComponent(type="LIFE_EXPECTANCY", adjustment=adjustment)
