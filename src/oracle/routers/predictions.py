from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from oracle.model import predict_life_expectancy

router = APIRouter(
    prefix="/predictions",
    responses={404: {"description": "Not found"}},
)


class UserInformation(BaseModel):
    age: int
    sex: Literal["M", "F"]


@router.post("/")
def create_item(user: UserInformation):
    return {"life_expectancy": predict_life_expectancy(user.age, user.sex)}
