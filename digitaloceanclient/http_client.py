from urllib.parse import urljoin 

import requests

from .exceptions import (
    NotFound, RateLimitExceeded, ServerError, Unauthorized
)


class HttpClient(object):
    base_url = 'https://api.digitalocean.com/v2/'

    def __init__(self, access_token):
        self.access_token = access_token

    def all(self):
        resource_name = self.__class__.__name__.lower()
        next_url = resource_name
        while True:
            response = self._request('GET', next_url)
            for row in response.get(resource_name, []):
                yield self.model.from_json(row)
            try:
                next_url = response['links']['pages']['next']
            except KeyError:
                break

    def _request(self, method, path):
        url = urljoin(self.base_url, path)
        f = getattr(requests, method.lower())
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }
        r = f(url, headers=headers)
        jsondata = r.json()

        if r.status_code == 200:
            # HTTP 200 - Ok
            return jsondata         
        elif r.status_code == 204:
            # HTTP 204 - No Content
            return 
        elif r.status_code == 401:
            # HTTP 401 - Unauthorized
            raise Unauthorized(jsondata.get('message'))
        elif r.status_code == 404:
            # HTTP 404 - Not Found
            raise NotFound(jsondata.get('message'))
        elif r.status_code == 429:
            # HTTP 429 - Too Many Requests
            raise RateLimitExceeded(jsondata.get('message'))
        elif r.status_code >= 500:
            # HTTP 500 - Internal Server Error
            raise ServerError(jsondata.get('message'))
