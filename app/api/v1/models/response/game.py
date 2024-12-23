from pydantic import BaseModel


class GameResponseModel(BaseModel):
    chat_id: int
    is_started: bool
