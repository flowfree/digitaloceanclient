from .http_client import HttpClient 
from .models import CDNEndpoint
from .exceptions import MalformedResponse


class CDNEndpoints(HttpClient):
    model = CDNEndpoint

    def all(self):
        """
        List all CDN endpoints.

        Yields
        ------
        digitaloceanclient.models.CDNEndpoint

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().all(path='cdn/endpoints')

    def create(self, origin, certificate_id=None, custom_domain=None, ttl=None):
        """
        Create a new CDN endpoint.

        Parameters
        ----------
        origin : str
            The fully qualified domain name (FQDN) for the origin server which 
            provides the content for the CDN.
        certificate_id : str, optional
            The ID of a DigitalOcean managed TLS certificate used for SSL when 
            a custom subdomain is provided.
        custom_domain : str, optional
            The fully qualified domain name (FQDN) of the custom subdomain to 
            be used with the CDN Endpoint. When used, a certificate_id must be 
            provided as well.
        ttl : int, optional
            The amount of time the content is cached by the CDN's edge servers 
            in seconds. Defaults to 3600s.

        Returns
        -------
        digitaloceanclient.models.CDNEndpoint

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'origin': origin}
        if certificate_id:
            payload['certificate_id'] = certificate_id
        if custom_domain:
            payload['custom_domain'] = custom_domain
        if ttl:
            payload['ttl'] = ttl
        response = self._request('POST', 'cdn/endpoints', payload=payload)
        try:
            return self.model(response['endpoint'])
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for CDNEndpoint.')

    def get(self, endpoint_id):
        """
        Retrieve an existing CDN endpoint.

        Parameters
        ----------
        endpoint_id : str
            The ID of the CDN endpoint to retrieve.

        Returns
        -------
        digitaloceanclient.models.CDNEndpoint

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        response = self._request('GET', f'cdn/endpoints/{endpoint_id}')
        try:
            return self.model(response['endpoint'])
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for CDNEndpoint.')

    def update(self, endpoint_id, certificate_id=None, custom_domain=None, ttl=None):
        """
        Update existing CDN endpoint.

        Parameters
        ----------
        endpoint_id : str
            The ID of the CDN endpoint to be updated.
        certificate_id : str, optional
            The ID of a DigitalOcean managed TLS certificate used for SSL when 
            a custom subdomain is provided.
        custom_domain : str, optional
            The fully qualified domain name (FQDN) of the custom subdomain to 
            be used with the CDN Endpoint. When used, a certificate_id must be 
            provided as well.
        ttl : int, optional
            The amount of time the content is cached by the CDN's edge servers 
            in seconds. Defaults to 3600s.

        Returns
        -------
        digitaloceanclient.models.CDNEndpoint

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {}
        if certificate_id:
            payload['certificate_id'] = certificate_id
        if custom_domain:
            payload['custom_domain'] = custom_domain
        if ttl:
            payload['ttl'] = ttl
        response = self._request('PUT', f'cdn/endpoints/{endpoint_id}', payload=payload)
        try:
            return self.model(response['endpoint'])
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for CDNEndpoint.')
