from typing import Annotated

from fastapi import Depends, Security
from fastapi.security import APIKeyHeader

from app.api.v1.exceptions.invalid_api_key_error import InvalidApiKeyError
from config import Config

config: Config = Config(_env_file=".env")


class Authenticator:
    master_api_key: str = config.api_key.get_secret_value()
    api_key_header: APIKeyHeader = APIKeyHeader(name="X-API-Key")

    @staticmethod
    def __verify_master_key(provided_api_key: Annotated[str, Security(api_key_header)]) -> None:
        if provided_api_key != Authenticator.master_api_key:
            raise InvalidApiKeyError("Provided API-key is invalid")

    verify_master_key: Depends = Depends(__verify_master_key)
