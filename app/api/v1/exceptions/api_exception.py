from starlette import status


class ApiError(Exception):
    status_code = status.HTTP_400_BAD_REQUEST
