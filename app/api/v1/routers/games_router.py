from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.api.v1.controllers.games_controller import GamesController
from app.api.v1.security.authenticator import Authenticator

games_router: APIRouter = APIRouter(prefix="/games", tags=["Games"])


@games_router.post(
    "/{chat_id}",
    status_code=status.HTTP_201_CREATED,
    dependencies=Authenticator.verify_master_key
)
async def create_game(
        chat_id: int,
        games_controller: Annotated[GamesController, Depends(GamesController.dependency)]
) -> None:
    await games_controller.create_game(chat_id)
