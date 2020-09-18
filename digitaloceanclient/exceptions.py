class Unauthorized(Exception):
    """HTTP 401 Error"""
    pass

class NotFound(Exception):
    """HTTP 404 Error"""
    pass


class ServerError(Exception):
    """HTTP 5xx Error"""
    pass
