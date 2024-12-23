from abc import ABC, abstractmethod
from typing import Any


class AbstractController(ABC):
    @abstractmethod
    async def _create(
            self,
            *args: Any,
            **kwargs: Any
    ) -> Any: pass

    @abstractmethod
    async def _get(
            self,
            *args: Any,
            **kwargs: Any
    ) -> Any: pass

    @abstractmethod
    async def _remove(
            self,
            *args: Any,
            **kwargs: Any
    ) -> Any: pass
