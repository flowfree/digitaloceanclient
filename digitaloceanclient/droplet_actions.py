from .exceptions import MalformedResponse
from .http_client import HttpClient 
from .models import DropletAction


class DropletActions(HttpClient):
    """
    Perform various tasks for droplets.
    """

    model = DropletAction

    def get(self, droplet_id, action_id):
        """
        Retrieve a droplet action.

        Parameters
        ----------
        droplet_id : str
            The ID of the droplet where this action takes place.
        action_id : str
            The unique identifier for the droplet action.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/{droplet_id}/actions/{action_id}'
        return self._request('GET', droplet_id, path=path)

    def enable_backups(self, droplet_id):
        """
        Enable backups on a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'enable_backups'}
        return self._request('POST', droplet_id, payload=payload)

    def enable_backups_for_tag(self, tag_name):
        """
        Enable backups for droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'enable_backups'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def disable_backups(self, droplet_id):
        """
        Disable backups on a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'disable_backups'}
        return self._request('POST', droplet_id, payload=payload)

    def disable_backups_for_tag(self, tag_name):
        """
        Disable backups for droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'disable_backups'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def reboot(self, droplet_id):
        """
        Reboot a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'reboot'}
        return self._request('POST', droplet_id, payload=payload)

    def power_cycle(self, droplet_id):
        """
        Power cycle a Droplet (power off and then back on).

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'power_cycle'}
        return self._request('POST', droplet_id, payload=payload)

    def power_cycle_for_tag(self, tag_name):
        """
        Power cycle droplets (power off and then back on).

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with this value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'power_cycle'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def shutdown(self, droplet_id):
        """
        Shut down a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'shutdown'}
        return self._request('POST', droplet_id, payload=payload)

    def shutdown_for_tag(self, tag_name):
        """
        Shutdown droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'shutdown'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def power_off(self, droplet_id):
        """
        Power off (hard shutdown) a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'power_off'}
        return self._request('POST', droplet_id, payload=payload)

    def power_off_for_tag(self, tag_name):
        """
        Power off droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'power_off'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def power_on(self, droplet_id):
        """
        Power on a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'power_on'}
        return self._request('POST', droplet_id, payload=payload)

    def power_on_for_tag(self, tag_name):
        """
        Power on droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'power_on'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def restore(self, droplet_id, image_slug):
        """
        Restore a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.
        image_slug : str
            The image that the droplet will use as a base.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'restore', 'image': image_slug}
        return self._request('POST', droplet_id, payload=payload)

    def password_reset(self, droplet_id):
        """
        Reset the password for a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'password_reset'}
        return self._request('POST', droplet_id, payload=payload)

    def resize(self, droplet_id, size_slug, disk=False):
        """
        Resize a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.
        size_slug : str
            The size slug that you want to resize to.
        disk : bool, optional
            Whether to increase disk size.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'type': 'resize', 
            'size': size_slug,
        }
        if disk:
            payload['disk'] = disk
        return self._request('POST', droplet_id, payload=payload)

    def rebuild(self, droplet_id, image_slug):
        """
        Rebuild a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.
        image_slug : str
            The image that the droplet will use as a base.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'type': 'rebuild',
            'image': image_slug,
        }
        return self._request('POST', droplet_id, payload=payload)

    def rename(self, droplet_id, name):
        """
        Rename a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.
        name : str
            The new name for the droplet

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'type': 'rename',
            'name': name,
        }
        return self._request('POST', droplet_id, payload=payload)

    def change_kernel(self, droplet_id, kernel):
        """
        Change the kernel of a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.
        kernel : int
            A unique number used to identify and reference a specific kernel.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'type': 'change_kernel',
            'kernel': kernel,
        }
        return self._request('POST', droplet_id, payload=payload)

    def enable_ipv6(self, droplet_id):
        """
        Enable IPv6 networking for a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'enable_ipv6'}
        return self._request('POST', droplet_id, payload=payload)

    def enable_ipv6_for_tag(self, tag_name):
        """
        Enable IPv6 networking for droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'enable_ipv6'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def snapshot(self, droplet_id, name=None):
        """
        Snapshot a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the specified droplet.
        name : str, optional
            The name for the snapshot

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {'type': 'snapshot'}
        if name:
            payload['name'] = name
        return self._request('POST', droplet_id, payload=payload)

    def snapshot_for_tag(self, tag_name):
        """
        Snapshot droplets.

        Parameters
        ----------
        tag_name : str
            Perform action on droplets tagged with the value.

        Returns
        -------
        list
            List of digitaloceanclient.models.DropletAction objects.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'droplets/actions?tag_name={tag_name}'
        payload = {'type': 'snapshot'}
        return self._request(method='POST', 
                             path=path, 
                             payload=payload)

    def _request(self, method, droplet_id=None, path=None, payload=None):
        if droplet_id is None and path is None:
            raise ValueError('Please specify droplet_id or path.')
        if not path:
            path = f'droplets/{droplet_id}/actions'
        response = super()._request(method, path, payload=payload)
        try:
            if droplet_id:
                return self.model(response['action'])
            else:
                return [self.model(x) for x in response['actions']]
        except (KeyError, ValueError, TypeError):
            raise MalformedResponse(f'Malformed response for Droplet Action.')

    def all(self, *args, **kwargs):
        raise NotImplementedError

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
