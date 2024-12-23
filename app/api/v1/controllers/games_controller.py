from app.api.v1.controllers.redis_controller import RedisController
from app.api.v1.exceptions.already_exists_error import AlreadyExistsError

from app.api.v1.models.game import GameModel


class GamesController(RedisController):
    async def create_game(
            self,
            chat_id: int
    ) -> GameModel | None:
        if await self._exists(f"games:{str(chat_id)}"):
            raise AlreadyExistsError(f"Game with chat ID {chat_id} already exists")

        game: GameModel = GameModel(chat_id=chat_id)

        await self._create(f"games:{str(chat_id)}", game.serialize())
        return game
