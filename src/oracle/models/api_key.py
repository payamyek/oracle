from uuid import UUID

from sqlmodel import Field, SQLModel


class ApiKey(SQLModel, table=True):
    client_id: UUID = Field(primary_key=True, foreign_key="client.id")
    name: str = Field(primary_key=True)
    hash: str
    referrer: str
    is_active: bool
    created_at: int
