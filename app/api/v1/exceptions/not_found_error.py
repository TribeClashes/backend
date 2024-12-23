from starlette import status

from app.api.v1.exceptions.api_error import ApiError


class NotFoundError(ApiError):
    status_code = status.HTTP_404_NOT_FOUND
