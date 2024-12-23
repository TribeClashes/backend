from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    api_key: SecretStr
    database_dsn: SecretStr | None = None
    redis_dsn: SecretStr
