from typing import Literal

from pydantic import BaseModel


class Prediction(BaseModel):
    age: int
    sex: Literal["M", "F"]


class PredictionResponse(BaseModel):
    life_expectancy: int
