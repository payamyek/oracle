from fastapi import FastAPI

from oracle import log
from oracle.routers import prediction

log.info("Application starting up ...")

app = FastAPI(redirect_slashes=False)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(router=prediction.router)
