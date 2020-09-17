import json 

import jsonpickle

from .http_client import HttpClient


class Droplets(HttpClient):
    py_object = 'digitaloceanclient.models.Droplet'

    def __init__(self, access_token):
        self.access_token = access_token

    def all(self):
        response = self._request('GET', 'droplets')
        for row in response.get('droplets', []):
            row['py/object'] = self.py_object
            yield jsonpickle.decode(json.dumps(row))

    def get(self, droplet_id):
        response = self._request('GET', f'droplets/{droplet_id}')
        data = response.get('droplet', {})
        data['py/object'] = self.py_object
        return jsonpickle.decode(json.dumps(data))

