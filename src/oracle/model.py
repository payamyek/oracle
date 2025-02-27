from typing import Literal

import pandas as pd
from pydantic import PositiveInt

# we cant estimate beyond this age
AGE_UPPER_BOUND = 110


def predict_life_expectancy(age: PositiveInt, sex: Literal["M", "F"]) -> int:
    if age > AGE_UPPER_BOUND:
        return age

    # get life table based on sex
    life_table = (
        pd.read_pickle("data/canada_male_life_table.pkl")
        if sex == "M"
        else pd.read_pickle("data/canada_female_life_table.pkl")
    )

    # determine life expectancy at the current age
    life_expectancy_at_age = life_table.query("age == @age")["e_x"].item()

    return int(age + life_expectancy_at_age)


print(predict_life_expectancy(age=111, sex="M"))
