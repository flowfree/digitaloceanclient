import json 

import jsonpickle

from .http_client import HttpClient


class Droplets(HttpClient):
    def __init__(self, access_token):
        self.access_token = access_token

    def all(self):
        data = self._request('GET', 'droplets')
        for row in data.get('droplets', []):
            row['py/object'] = 'digitaloceanclient.models.Droplet'
            yield jsonpickle.decode(json.dumps(row))

