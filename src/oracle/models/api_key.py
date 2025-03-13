from sqlmodel import Field, SQLModel


class ApiKey(SQLModel, table=True):
    client_id: str = Field(primary_key=True)
    name: str = Field(primary_key=True)
    hash: str
    referrer: str
    is_active: bool
    created_at: int
