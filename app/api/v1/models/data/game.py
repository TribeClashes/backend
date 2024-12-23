from typing import Dict, Any


class Game:
    def __init__(
            self,
            chat_id: int,
            *,
            is_started: bool | None = None
    ) -> None:
        self.chat_id: int = chat_id
        self.is_started: bool = is_started or False

    @classmethod
    def from_serialized(
            cls,
            serialized: Dict[str, Any]
    ) -> 'Game':
        return cls(
            serialized["chat_id"],
            is_started=serialized.get("is_started")
        )

    @property
    def serialized(self) -> Dict[str, Any]:
        return {
            "chat_id": self.chat_id,
            "is_started": self.is_started
        }
