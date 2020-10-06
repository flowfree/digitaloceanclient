from .http_client import HttpClient
from .models import Certificate


class Certificates(HttpClient):
    model = Certificate

    def all(self):
        """
        List all certificates.

        Yields
        ------
        digitaloceanclient.models.Certificate

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().all()

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
