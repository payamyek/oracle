from fastapi import FastAPI

from oracle import log
from oracle.routers import predictions

log.info("Application starting up ...")

app = FastAPI(redirect_slashes=False)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(router=predictions.router)
