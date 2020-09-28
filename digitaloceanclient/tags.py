from .http_client import HttpClient
from .models import Tag


class Tags(HttpClient):
    model = Tag 

    def create(self, name):
        payload = dict(name=name)
        return super().create(payload=payload)
