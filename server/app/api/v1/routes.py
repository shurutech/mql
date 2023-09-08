from fastapi import APIRouter

from app.api.v1 import authentication, databases, query

api_router = APIRouter()
api_router.include_router(authentication.router, prefix="/v1", tags=["authentication"])
api_router.include_router(databases.router, prefix="/v1", tags=["databases"])
api_router.include_router(query.router, prefix="/v1", tags=["query"])
