from fastapi import APIRouter

router = APIRouter(tags=["Core"])


@router.get("/health")
def health_check():
    return {"status": "healthy"}
