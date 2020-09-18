from urllib.parse import urljoin 

import requests

from .exceptions import (
    Unauthorized, NotFound
)


class HttpClient(object):
    base_url = 'https://api.digitalocean.com/v2/'

    def __init__(self, access_token):
        self.access_token = access_token

    def _request(self, method, path):
        url = urljoin(self.base_url, path)
        f = getattr(requests, method.lower())
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }
        r = f(url, headers=headers)
        jsondata = r.json()
        if r.status_code == 401:
            raise Unauthorized(jsondata.get('message'))
        elif r.status_code == 404:
            raise NotFound(jsondata.get('message'))
        return jsondata
