from datetime import date, datetime
from functools import cached_property
from typing import Literal

from pydantic import BaseModel, Field, computed_field


def _calculate_age(date_of_birth: date) -> int:
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))


class PredictionCreate(BaseModel):
    date_of_birth: date
    sex: Literal["M", "F"]
    country_code: Literal["CA"] = Field(description="Country code adhering to ISO 3166-1 alpha-2")

    @computed_field
    @cached_property
    def age(self) -> int:
        return _calculate_age(self.date_of_birth)


class PredictionPublic(BaseModel):
    life_expectancy: int = Field(ge=0)
    date_of_birth: date

    @computed_field
    @cached_property
    def date_of_death(self) -> date:
        age = _calculate_age(self.date_of_birth)
        return date(self.life_expectancy - age + date.today().year, 1, 1)

    @computed_field
    @cached_property
    def milliseconds_till_death(self) -> int:
        return int(
            (datetime.combine(self.date_of_death, datetime.min.time()) - datetime.now()).total_seconds() * 1000.0
        )
