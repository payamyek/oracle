import hashlib
from typing import Annotated

from fastapi import Depends, Header, HTTPException
from pydantic import UUID4, BaseModel
from sqlmodel import Session, select

from oracle import database_engine
from oracle.models.api_key import ApiKey


def get_session():
    with Session(database_engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


class CommonHeaders(BaseModel):
    referer: str
    x_client_id: UUID4
    x_api_key: str


CommonHeadersDep = Annotated[CommonHeaders, Header()]


async def verify_api_key(headers: CommonHeadersDep, session: SessionDep):
    results = session.exec(select(ApiKey).where(ApiKey.client_id == headers.x_client_id)).all()

    for record in results:
        hashed_api_key = hashlib.sha256((headers.x_api_key + record.salt).encode()).hexdigest()
        if (hashed_api_key, headers.referer) == (record.hashed_api_key, record.referer):
            return

    raise HTTPException(status_code=403, detail="API key is invalid")


VerifyApiKeyDep = Depends(verify_api_key)
