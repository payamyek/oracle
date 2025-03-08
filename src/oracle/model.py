import pandas as pd

from oracle.schemas.predictions import Prediction

# can't estimate beyond this age
AGE_UPPER_BOUND = 110


def predict_life_expectancy(prediction: Prediction) -> int:
    if prediction.age > AGE_UPPER_BOUND:
        return prediction.age

    # get life table based on sex
    life_table = (
        pd.read_pickle("data/canada_male_life_table.pkl")
        if prediction.sex == "M"
        else pd.read_pickle("data/canada_female_life_table.pkl")
    )

    # determine life expectancy at the current age
    life_expectancy_at_age = life_table.query("age == @prediction.age")["e_x"].item()

    return int(prediction.age + life_expectancy_at_age)
