from .http_client import HttpClient
from .models import FloatingIP


class FloatingIPs(HttpClient):
    """
    Retrieve, create, and delete Floating IPs.
    """

    model = FloatingIP

    def all(self):
        """
        List all floating IPs available on current user's account.

        Yields
        ------
        digitaloceanclient.models.FloatingIP

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().all(path='floating_ips')

    def create(self, droplet_id=None, region_slug=None):
        """
        Create a new floating IP assigned to a Droplet or reserved to a region.

        Parameters
        ----------
        droplet_id : str, optional
            The ID of the droplet that the floating IP will be assigned to.
        region_slug : str, optional
            The slug for the region the floating IP will be reserved to.

        Returns
        -------
        digitaloceanclient.models.FloatingIP

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        if droplet_id is None and region_slug is None:
            raise ValueError('Please specify droplet_id or region_slug.')
        payload = {}
        if droplet_id and len(payload) == 0:
            payload['droplet_id'] = droplet_id
        if region_slug and len(payload) == 0:
            payload['region'] = region_slug
        return super().create(path='floating_ips', payload=payload)

    def get(self, floating_ip_addr):
        """
        Retrieve an existing floating IP.

        Parameters
        ----------
        floating_ip_addr : str
            The IP address of the floating IP.

        Returns
        -------
        digitaloceanclient.models.FloatingIP

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().get(resource_id=floating_ip_addr, 
                           path='floating_ips')

    def delete(self, floating_ip_addr):
        """
        Delete a floating IP.

        Parameters
        ----------
        floating_ip_addr : str
            The IP address of the floating IP.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().delete(resource_id=floating_ip_addr,
                              path='floating_ips')

    def update(self, *args, **kwargs):
        raise NotImplementedError
