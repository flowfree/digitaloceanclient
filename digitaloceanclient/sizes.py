from .http_client import HttpClient
from .models import Size


class Sizes(HttpClient):
    model = Size
