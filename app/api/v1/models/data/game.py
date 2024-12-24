from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Game:
    chat_id: int
    is_started: bool = False

    @classmethod
    def from_serialized(
            cls,
            serialized: Dict[str, Any]
    ) -> 'Game':
        return cls(
            chat_id=serialized["chat_id"],
            is_started=serialized["is_started"]
        )

    @property
    def serialized(self) -> Dict[str, Any]:
        return {
            "chat_id": self.chat_id,
            "is_started": self.is_started
        }
