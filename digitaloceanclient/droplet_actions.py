from .http_client import HttpClient 
from .models import DropletAction


class DropletActions(HttpClient):
    """
    Perform various tasks for droplets.
    """

    model = DropletAction

    def get(self, action_id):
        """
        Retrieve a droplet action.

        Parameters
        ----------
        action_id : str
            The unique identifier for the droplet action.

        Returns
        -------
        digitaloceanclient.models.DropletAction

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

    def resize(self, droplet_id, size_slug, disk=None):
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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

    def all(self, *args, **kwargs):
        raise NotImplementedError

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
