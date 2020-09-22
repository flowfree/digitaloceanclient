from urllib.parse import urljoin 

import requests

from .exceptions import (
    APIError, BadRequest, MalformedResponse, NotFound, RateLimitExceeded, 
    ServerError, Unauthorized
)


class HttpClient(object):
    base_url = 'https://api.digitalocean.com/v2/'

    def __init__(self, access_token):
        self.access_token = access_token

    def all(self, params=None):
        resource_name = self.__class__.__name__.lower()
        next_url = resource_name
        while True:
            response = self._request('GET', next_url, params)
            for row in response.get(resource_name, []):
                yield self.model(row)
            try:
                next_url = response['links']['pages']['next']
            except KeyError:
                break

    def _request(self, method, path, params=None, payload=None):
        url = urljoin(self.base_url, path)
        f = getattr(requests, method.lower())
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }
        r = f(url, headers=headers, params=params, json=payload)
        try:
            jsondata = r.json()
        except Exception:
            raise MalformedResponse('Invalid JSON response')

        if r.status_code in [200, 202]:
            # HTTP 200 - Ok
            # HTTP 202 - Accepted
            return jsondata         
        elif r.status_code == 204:
            # HTTP 204 - No Content
            return 
        elif r.status_code == 400:
            # HTTP 400 - Bad Request
            raise BadRequest(jsondata.get('message'))
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
        else:
            api_error = APIError(jsondata.get('message', 'Unknown error'))
            api_error.status_code = r.status_code
            raise api_error
