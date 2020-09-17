import json 

from .http_client import HttpClient
from .models import Droplet


class Droplets(HttpClient):
    def __init__(self, access_token):
        self.access_token = access_token

    def all(self):
        response = self._request('GET', 'droplets')
        for row in response.get('droplets', []):
            yield Droplet.from_json(row)

    def get(self, droplet_id):
        response = self._request('GET', f'droplets/{droplet_id}')
        data = response.get('droplet', {})
        return Droplet.from_json(data)

