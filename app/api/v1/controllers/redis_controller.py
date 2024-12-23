import json
from typing import Annotated, Any

from fastapi import Depends
from redis import Redis

from app.api.v1.controllers.abstract_controller import AbstractController
from app.dependencies import Dependency


class RedisController(AbstractController):
    def __init__(
            self,
            redis: Redis
    ) -> None:
        self.redis: Redis = redis

    async def _create(
            self,
            key: str,
            value: Any
    ) -> None:
        serialized: str = json.dumps(value)
        await self.redis.set(f"tribeclashes:{key}", serialized)

    async def _get(
            self,
            key: str
    ) -> Any:
        serialized: str = await self.redis.get(f"tribeclashes:{key}")
        return json.loads(serialized) if serialized is not None else None

    async def _exists(
            self,
            key: str
    ) -> bool:
        return bool(await self.redis.exists(f"tribeclashes:{key}"))

    async def _remove(
            self,
            key: str
    ) -> None:
        await self.redis.delete(f"tribeclashes:{key}")

    @classmethod
    async def dependency(
            cls,
            redis: Annotated[Redis, Depends(Dependency.redis)]
    ) -> 'RedisController':
        return cls(redis)
