from .http_client import HttpClient
from .models import Region


class Regions(HttpClient):
    model = Region
