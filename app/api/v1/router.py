from fastapi import APIRouter

from app.api.v1.routers.games_router import games_router

v1_router: APIRouter = APIRouter(prefix="/v1")
v1_router.include_router(games_router)
