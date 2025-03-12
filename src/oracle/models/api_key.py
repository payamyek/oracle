from sqlmodel import Field, SQLModel


class ApiKey(SQLModel, table=True):
    clientId: str = Field(primary_key=True)
    name: str = Field(primary_key=True)
    hash: str
    referrer: str
    isActive: bool
    createdTimestamp: int
