from urllib.parse import urljoin, urlparse

import requests

from .exceptions import (
    APIError, BadRequest, MalformedResponse, NotFound, RateLimitExceeded, 
    ServerError, Unauthorized, UnprocessableEntity
)


class HttpClient(object):
    """
    Base class for making HTTP requests to the DigitalOcean REST API.

    Attributes
    ----------
    base_url : str
        The base URL for the API endpoints.
    """

    base_url = 'https://api.digitalocean.com/v2/'

    def __init__(self, access_token):
        """
        Parameters
        ----------
        access_token : str
            The access token for the DigitalOcean REST API.
        """
        self.access_token = access_token

    def all(self, path=None, params=None):
        """
        Retrieve the collection of a resource.

        Parameters
        ----------
        path : str, optional
            The path to the API endpoint. If not specified, it will derived 
            from the class name.
        params : dict, optional
            The querystring of the request URL.

        Yields
        ------
        digitaloceanclient.Model
            The model specified in the class that inherits this base class.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        resource_name = self.__class__.__name__.lower()
        if path:
            next_url = path
        else:
            next_url = resource_name
        while True:
            response = self._request('GET', next_url, params)
            key = urlparse(next_url).path.split('/')[-1]
            for row in response.get(key, []):
                yield self.model(row)
            try:
                next_url = response['links']['pages']['next']
            except KeyError:
                break

    def create(self, path=None, payload=None):
        """
        Create a new resource.

        Parameters
        ----------
        path : str, optional
            The path of the API endpoint. If not supplied, it will be 
            determined from the resource class name.
        payload : dict, optional
            The dict for the JSON payload 

        Returns
        -------
        digitaloceanclient.models.Model
            The model for the specified resource.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        if not path:
            path = self.__class__.__name__.lower()
        response = self._request('POST', path, payload=payload)
        try:
            model_name = self.model.__name__.lower()
            return self.model(response[model_name])
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for {model_name.title()}')

    def get(self, resource_id):
        """
        Retrieve a resource.

        Parameters
        ----------
        resource_id : str
            The ID of the specified resource.

        Returns
        -------
        digitaloceanclient.models.Model
            The model for the specified resource.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        resource_name = self.__class__.__name__.lower()
        response = self._request('GET', f'{resource_name}/{resource_id}')
        try:
            model_name = self.model.__name__.lower()
            return self.model(response[model_name])
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for {model_name.title()}')

    def update(self, resource_id, payload=None):
        """
        Update an existing resource.

        Parameters
        ----------
        resource_id : str, optional
            The ID of the resource to be updated.
        payload : dict, optional
            The dict for the JSON payload,

        Returns
        -------
        digitaloceanclient.models.Model
            The model for the specified resource.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        resource_name = self.__class__.__name__.lower()
        response = self._request('PUT', f'{resource_name}/{resource_id}', payload=payload)
        try:
            model_name = self.model.__name__.lower()
            return self.model(response[model_name])
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for {model_name.title()}')

    def delete(self, resource_id):
        """
        Delete a resource.

        Parameters
        ----------
        resource_id : str
            The ID of the specified resource.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        resource_name = self.__class__.__name__.lower()
        response = self._request('DELETE', f'{resource_name}/{resource_id}')

    def _request(self, method, path, params=None, payload=None):
        """
        Make the HTTP request.

        Parameters
        ----------
        method : {"GET", "POST", "PUT", "DELETE"}
            The HTTP method to be used.
        path : str
            The path the the endpoint API.
        params : dict, optional
            The querystring for the request.
        payload : dict, optional
            The JSON payload for the request body.

        Returns
        -------
        dict, optional
            The JSON response from the API or None if no response returned.

        Raises
        ------
        digitaloceanclient.exceptions.BadRequest
            When the request body is invalid.
        digitalcoeanclient.exceptions.Unauthorized
            When the access token is invalid.
        digitalcoeanclient.exceptions.NotFound
            When it hit unrecognized URL endpoint.
        digitalcoeanclient.exceptions.UnprocessableEntity
            When the request is okay but the API cannot further process it.
        digitalcoeanclient.exceptions.RateLimitExceeded
            When the API receives too many requests.
        digitalcoeanclient.exceptions.ServerError
            When the API experiencing internal server error.
        digitalcoeanclient.exceptions.APIError
            For other HTTP 4xx and 5xx errors.
        """

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
