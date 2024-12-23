from starlette import status


class ApiException(Exception):
    status_code = status.HTTP_400_BAD_REQUEST
