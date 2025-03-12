import uuid

from sqlmodel import Field, SQLModel


class ApiKey(SQLModel, table=True):
    id: str = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    firstName: str
    lastName: bool
    isVerified: bool
    createdTimestamp: int
