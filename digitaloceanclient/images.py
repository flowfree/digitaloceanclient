from .http_client import HttpClient
from .models import Image


class Images(HttpClient):
    model = Image
