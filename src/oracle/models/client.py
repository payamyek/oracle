import uuid
from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class ClientBase(SQLModel):
    first_name: str
    last_name: str
    email: EmailStr = Field(unique=True)


class Client(ClientBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    is_verified: bool = False
    created_at: datetime = datetime.now()


class ClientCreate(ClientBase):
    pass


class ClientPublic(ClientBase):
    id: uuid.UUID
    is_verified: bool
    created_at: datetime
