from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from redis.asyncio import Redis
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api.router import api_router
from app.api.v1.exceptions.api_error import ApiError
from app.dependencies import Dependency
from config import Config

config: Config = Config(_env_file=".env")


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    database = None
    redis: Redis = Redis.from_url(config.redis_dsn.get_secret_value())

    Dependency.inject(
        fastapi_app,
        database,
        redis
    )

    yield

    await redis.aclose()

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.exception_handler(ApiError)
async def api_exception_handler(request: Request, exc: ApiError):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"detail": str(exc)}),
    )


@app.exception_handler(Exception)
async def api_server_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"detail": str(exc)}),
    )


