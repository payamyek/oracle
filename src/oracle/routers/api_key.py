from fastapi import APIRouter

from oracle.dependencies import SessionDep
from oracle.models.api_key import ApiKey

router = APIRouter(
    prefix="/api/v1/api-keys",
)


@router.post("")
def create_api_key(api_key: ApiKey, session: SessionDep) -> ApiKey:
    db_api_key = ApiKey.model_validate(api_key)

    session.add(db_api_key)
    session.commit()
    session.refresh(db_api_key)
    return db_api_key
