from .http_client import HttpClient
from .models import FloatingIPAction


class FloatingIPActions(HttpClient):
    """
    Perform various tasks for Floating IPs.
    """

    model = FloatingIPAction

    def all(self, for_ip_addr):
        """
        List all actions for a Floating IP.

        Parameters
        ----------
        for_ip_addr : str
            The address of the Floating IP.

        Yields
        ------
        digitaloceanclient.models.FloatingIPAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'floating_ips/{for_ip_addr}/actions'
        return super().all(path=path)

    def assign(self, for_ip_addr, droplet_id):
        """
        Assign a Floating IP to a Droplet.

        Parameters
        ----------
        for_ip_addr : str
            The address of the Floating IP.
        droplet_id : str
            The ID of the droplet that the floating IP will 
            be assigned to.

        Returns
        -------
        digitaloceanclient.models.FloatingAPIAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'floating_ips/{for_ip_addr}/actions'
        payload = {
            'type': 'assign',
            'droplet_id': droplet_id,
        }
        return super().create(path=path, payload=payload)

    def unassign(self, for_ip_addr):
        """
        Unassign a Floating IP from droplet.

        Parameters
        ----------
        for_ip_addr : str
            The address of the Floating IP.

        Returns
        -------
        digitaloceanclient.models.FloatingAPIAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'floating_ips/{for_ip_addr}/actions'
        payload = {'type': 'unassign'}
        return super().create(path=path, payload=payload)

    def get(self, for_ip_addr, action_id):
        """
        Retrieve an existing Floating IP Action.

        Parameters
        ----------
        for_ip_addr : str
            The address of the Floating IP.
        action_id : str
            The ID of the Floating IP Action to retrieve.

        Returns
        -------
        digitaloceanclient.models.FloatingIPAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'floating_ips/{for_ip_addr}/actions'
        return super().get(path=path, resource_id=action_id)

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
