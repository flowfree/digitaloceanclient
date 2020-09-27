from .http_client import HttpClient
from .models import Tag


class Tags(HttpClient):
    model = Tag 
