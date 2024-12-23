from starlette import status

from app.api.v1.exceptions.api_error import ApiError


class InvalidApiKeyError(ApiError):
    status_code = status.HTTP_401_UNAUTHORIZED
