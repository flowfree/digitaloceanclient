from urllib.parse import urljoin 

import requests


class HttpClient(object):
    base_url = 'https://api.digitalocean.com/v2/'

    def __init__(self, access_token):
        self.access_token = access_token

    def _request(self, method, path):
        url = urljoin(self.base_url, path)
        f = getattr(requests, method.lower())
        r = f(url, headers={'Authorization': f'Bearer {self.access_token}'})
        return r.json()
