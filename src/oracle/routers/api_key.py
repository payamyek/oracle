import hashlib
import uuid

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from oracle.dependencies import SessionDep
from oracle.models.api_key import ApiKey, ApiKeyCreate, ApiKeyPublic
from oracle.models.client import Client

router = APIRouter(prefix="/api/v1/api-keys", tags=["API Keys"])


@router.post("", response_model=ApiKeyPublic)
def create_api_key(api_key: ApiKeyCreate, session: SessionDep):
    statement = select(Client).where(Client.id == api_key.client_id)
    results = session.exec(statement)
    client = results.first()

    if not client:
        raise HTTPException(status_code=404, detail=f"Client with {api_key.client_id=} does not exist")
    elif not client.is_verified:
        raise HTTPException(status_code=403, detail="Unverified client cannot make API keys")

    raw_api_key = hashlib.sha256((api_key.referrer + api_key.client_id.hex + uuid.uuid4().hex).encode()).hexdigest()
    salt = uuid.uuid4().hex
    hashed_api_key = hashlib.sha256((raw_api_key + salt).encode()).hexdigest()

    db_api_key = ApiKey.model_validate(api_key, update={"hashed_api_key": hashed_api_key, "salt": salt})
    session.add(db_api_key)
    session.commit()
    session.refresh(db_api_key)

    return db_api_key.model_dump() | {"api_key": raw_api_key}
