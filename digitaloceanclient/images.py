from .http_client import HttpClient
from .models import Image


class Images(HttpClient):
    def all(self):
        next_url = 'images'
        while True:
            response = self._request('GET', next_url)
            for row in response.get('images', []):
                yield Image.from_json(row)
            try:
                next_url = response['links']['pages']['next']
            except KeyError:
                break
