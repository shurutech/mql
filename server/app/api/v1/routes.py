from fastapi import APIRouter

from app.api.v1 import authentication, databases, query, query_executor

api_router = APIRouter()
api_router.include_router(authentication.router, prefix="/api/v1", tags=["authentication"])
api_router.include_router(databases.router, prefix="/api/v1", tags=["databases"])
api_router.include_router(query.router, prefix="/api/v1", tags=["query"])
api_router.include_router(query_executor.router, prefix="/api/v1", tags=["data-query-service"])
