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


class _CommonHeaders(BaseModel):
    referer: str
    x_client_id: UUID4
    x_api_key: str


CommonHeaders = Annotated[_CommonHeaders, Header()]


async def verify_api_key(headers: CommonHeaders, session: SessionDep):
    api_keys = session.exec(select(ApiKey).where(ApiKey.client_id == headers.x_client_id)).all()

    found = False

    for api_key in api_keys:
        hashed_api_key = hashlib.sha256((headers.x_api_key + api_key.salt).encode()).hexdigest()
        if hashed_api_key == api_key.hashed_api_key and headers.referer == api_key.referrer:
            found = True
            break

    if not found:
        raise HTTPException(status_code=403, detail="API key is invalid")


VerifyApiKeyDep = Depends(verify_api_key)
