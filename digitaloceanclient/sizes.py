from .http_client import HttpClient
from .models import Size


class Sizes(HttpClient):
    def all(self):
        response = self._request('GET', 'sizes')
        for row in response.get('sizes', []):
            yield Size.from_json(row)
