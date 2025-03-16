from datetime import datetime
from uuid import UUID

from sqlmodel import Field, SQLModel


class ApiKeyBase(SQLModel):
    name: str = Field(primary_key=True)
    referrer: str


class ApiKey(ApiKeyBase, table=True):
    client_id: UUID = Field(primary_key=True, foreign_key="client.id")
    hashed_api_key: str
    salt: str
    is_active: bool = True
    created_at: datetime = datetime.now()


class ApiKeyCreate(ApiKeyBase):
    client_id: UUID
    pass


class ApiKeyPublic(SQLModel):
    name: str
    api_key: str
    is_active: bool
    created_at: datetime
