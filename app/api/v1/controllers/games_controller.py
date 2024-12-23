from typing import Dict, Any

from app.api.v1.controllers.redis_controller import RedisController
from app.api.v1.exceptions.already_exists_error import AlreadyExistsError
from app.api.v1.exceptions.not_found_error import NotFoundError
from app.api.v1.models.data.game import Game


class GamesController(RedisController):
    async def create_game(
            self,
            chat_id: int
    ) -> Game | None:
        if await self._exists(f"games:{chat_id}"):
            raise AlreadyExistsError(f"Game with chat ID {chat_id} already exists")

        game: Game = Game(chat_id=chat_id)

        await self._create(f"games:{chat_id}", game.serialized)
        return game

    async def get_game(
            self,
            chat_id: int
    ) -> Game | None:
        game: Dict[str, Any] | None = await self._get(f"games:{chat_id}")

        if game is None:
            raise NotFoundError(f"Game with chat ID {chat_id} was not found")

        return Game.from_serialized(game)

    async def remove_game(
            self,
            chat_id: int
    ) -> None:
        if not await self._exists(f"games:{chat_id}"):
            raise NotFoundError(f"Game with chat ID {chat_id} was not found")

        await self._remove(f"games:{chat_id}")
