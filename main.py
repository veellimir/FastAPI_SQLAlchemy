from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from dependecies.functions import init_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_service(app)
    yield


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
