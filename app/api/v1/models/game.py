from typing import Dict, Any

from pydantic import BaseModel


class GameModel(BaseModel):
    chat_id: int
    is_started: bool = False

    @classmethod
    def from_serialized(
            cls,
            game: Dict[str, Any]
    ) -> 'GameModel':
        return GameModel(
            chat_id=game["chat_id"],
            is_started=game["is_started"]
        )

    def serialize(self) -> Dict[str, Any]:
        return {
            "chat_id": self.chat_id,
            "is_started": self.is_started
        }
