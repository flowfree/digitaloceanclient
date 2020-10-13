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

    def create(self, name, ip_address=None):
        """
        Create a new domain.

        Parameters
        ----------
        name : str
            The domain name to add to the DigitalOcean DNS management 
            interface.
        ip_address: str, optional
            When provided, an A record will be automatically created 
            pointing to the domain.

        Returns
        -------
        digitaloceanclient.models.Domain

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'name': name}
        if ip_address:
            payload['ip_address'] = ip_address
        return super().create(payload=payload)

    def get(self, name):
        """
        Retrieve existing domain.

        Parameters
        ----------
        name : str
            The name of the domain

        Returns
        -------
        digitaloceanclient.models.Domain

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().get(resource_id=name)

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
