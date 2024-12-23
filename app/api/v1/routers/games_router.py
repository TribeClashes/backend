from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.api.v1.controllers.games_controller import GamesController
from app.api.v1.models.data.game import Game
from app.api.v1.models.response.game import GameResponseModel
from app.api.v1.security.authenticator import Authenticator

games_router: APIRouter = APIRouter(prefix="/games", tags=["Games"])


@games_router.post(
    "/{chat_id}",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Authenticator.verify_master_key]
)
async def create_game(
        chat_id: int,
        games_controller: Annotated[GamesController, Depends(GamesController.dependency)]
) -> GameResponseModel:
    game: Game = await games_controller.create_game(chat_id)

    return GameResponseModel(
        chat_id=game.chat_id,
        is_started=game.is_started
    )


@games_router.get(
    "/{chat_id}",
    status_code=status.HTTP_200_OK,
    response_model=GameResponseModel,
    dependencies=[Authenticator.verify_master_key]
)
async def get_game(
        chat_id: int,
        games_controller: Annotated[GamesController, Depends(GamesController.dependency)]
) -> GameResponseModel:
    game: Game = await games_controller.get_game(chat_id)

    return GameResponseModel(
        chat_id=game.chat_id,
        is_started=game.is_started
    )


@games_router.delete(
    "/{chat_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Authenticator.verify_master_key]
)
async def remove_game(
        chat_id: int,
        games_controller: Annotated[GamesController, Depends(GamesController.dependency)]
) -> None:
    await games_controller.remove_game(chat_id)
