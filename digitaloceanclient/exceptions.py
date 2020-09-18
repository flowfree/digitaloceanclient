class Unauthorized(Exception):
    status_code = 401


class NotFound(Exception):
    status_code = 404


class ServerError(Exception):
    status_code = 500


class RateLimitExceeded(Exception):
    status_code = 429
