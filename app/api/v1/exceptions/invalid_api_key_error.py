from starlette import status

from app.api.v1.exceptions.api_exception import ApiError


class InvalidApiKeyError(ApiError):
    status_code = status.HTTP_401_UNAUTHORIZED
