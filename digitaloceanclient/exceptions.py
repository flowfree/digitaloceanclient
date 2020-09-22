class APIError(Exception):
    status_code = None


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
