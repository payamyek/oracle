from typing import Literal

import pandas as pd
from pydantic import PositiveInt


def predict_life_expectancy(age: PositiveInt, sex: Literal["M", "F"]) -> int:
    # get life table based on sex
    life_table = (
        pd.read_pickle("data/canada_male_life_table.pkl")
        if sex == "M"
        else pd.read_pickle("data/canada_female_life_table.pkl")
    )

    # determine life expectancy at the current age
    life_expectancy_at_age = life_table.query("age == @age")["e_x"].item()

    return int(age + life_expectancy_at_age)
