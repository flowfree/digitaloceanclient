from .http_client import HttpClient
from .models import Region


class Regions(HttpClient):
    def all(self):
        response = self._request('GET', 'regions')
        for row in response.get('regions', []):
            yield Region.from_json(row)
