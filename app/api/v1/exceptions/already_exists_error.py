from starlette import status

from app.api.v1.exceptions.api_error import ApiError


class AlreadyExistsError(ApiError):
    status_code = status.HTTP_409_CONFLICT
