from fastapi import FastAPI
from app.api.v1.routes import api_router
from fastapi.middleware.cors import CORSMiddleware
from logging.config import dictConfig
import logging
from app.core.log_config import log_config

dictConfig(log_config)

app = FastAPI(
    # docs_url=None,
    # redoc_url=None
)

logger = logging.getLogger("analytics")


@app.get("/ping")
async def ping_health():
    logger.info("Ping health check")
    return {"message": "OK"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["x-auth-token"],
)

app.include_router(api_router)
