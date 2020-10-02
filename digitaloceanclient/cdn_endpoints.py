from .http_client import HttpClient 
from .models import CDNEndpoint


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
