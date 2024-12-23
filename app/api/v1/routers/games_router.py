from fastapi import APIRouter
from starlette import status

from app.api.v1.security.authenticator import Authenticator

games_router: APIRouter = APIRouter(prefix="/games", tags=["Games"])


@games_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=Authenticator.verify_master_key
)
async def create_game() -> None:
    pass
