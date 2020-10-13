from .http_client import HttpClient
from .models import Domain


class Domains(HttpClient):
    model = Domain

    def all(self):
        """
        Get all domains in current user's account.

        Yields
        ------
        digitaloceanclient.models.Domain

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
