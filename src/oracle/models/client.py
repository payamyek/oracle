from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class ClientBase(SQLModel):
    first_name: str
    last_name: str


class Client(ClientBase, table=True):
    email: EmailStr = Field(primary_key=True)
    is_verified: bool = False
    created_at: datetime = datetime.now()
