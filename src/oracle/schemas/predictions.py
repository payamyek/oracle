from datetime import date
from functools import cached_property
from typing import Literal

from pydantic import BaseModel, Field, computed_field


class Prediction(BaseModel):
    date_of_birth: date
    sex: Literal["M", "F"]

    @computed_field
    @cached_property
    def age(self) -> int:
        return int((date.today() - self.date_of_birth).days / 365)


class PredictionResponse(BaseModel):
    life_expectancy: int = Field(ge=0)
