class APIError(Exception):
    status_code = None
    message = ''

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        if status_code:
            self.status_code = status_code

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}: {self.message}'


class BadRequest(APIError):
    status_code = 400


class Unauthorized(APIError):
    status_code = 401


class NotFound(APIError):
    status_code = 404


class ServerError(APIError):
    status_code = 500


class RateLimitExceeded(APIError):
    status_code = 429


class MalformedResponse(APIError):
    pass
