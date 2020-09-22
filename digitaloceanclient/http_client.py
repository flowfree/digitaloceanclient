from urllib.parse import urljoin 

import requests

from .exceptions import (
    APIError, BadRequest, MalformedResponse, NotFound, RateLimitExceeded, 
    ServerError, Unauthorized, UnprocessableEntity
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
        if r.status_code != 204:
            try:
                jsondata = r.json()
            except Exception:
                raise MalformedResponse('Invalid JSON response')

        if r.status_code in [200, 201, 202]:
            # HTTP 200 - Ok
            # HTTP 201 - Created
            # HTTP 202 - Accepted
            return jsondata
        elif r.status_code == 204:
            # HTTP 204 - No Content
            return 
        error_message = jsondata.get('message', 'Unknown error')
        if r.status_code == 400:
            # HTTP 400 - Bad Request
            raise BadRequest(error_message)
        elif r.status_code == 401:
            # HTTP 401 - Unauthorized
            raise Unauthorized(error_message)
        elif r.status_code == 404:
            # HTTP 404 - Not Found
            raise NotFound(error_message)
        elif r.status_code == 422:
            # HTTP 422 - Unprocessable Entity
            raise UnprocessableEntity(error_message)
        elif r.status_code == 429:
            # HTTP 429 - Too Many Requests
            raise RateLimitExceeded(error_message)
        elif r.status_code >= 500:
            # HTTP 500 - Internal Server Error
            raise ServerError(error_message)
        else:
            raise APIError(error_message, r.status_code)
