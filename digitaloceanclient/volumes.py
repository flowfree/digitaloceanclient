from .http_client import HttpClient
from .models import Volume


class Volumes(HttpClient):
    model = Volume

    def all(self, name=None):
        """
        List all block storage volumes.

        Paramters
        ---------
        name : str, optional
            Filter by the given name

        Yields
        ------
        digitaloceanclient.models.Volume
        """

        if name:
            params = {'name': name}
        else:
            params = None
        return super().all(params=params)
