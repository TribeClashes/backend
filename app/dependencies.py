from fastapi import FastAPI
from starlette.requests import Request


class DependencyManager:
    @staticmethod
    def inject(
            fastapi_app: FastAPI,
            database,
            redis
    ) -> None:
        pass

    @staticmethod
    def database(request: Request) -> None:
        pass

    @staticmethod
    def redis(request: Request) -> None:
        pass
