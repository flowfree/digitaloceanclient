from .http_client import HttpClient
from .models import Volume
from .models import Snapshot
from .exceptions import MalformedResponse


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

    def create(self, name, region, size_gigabytes, description=None, snapshot_id=None, 
              filesystem_type=None, filesystem_label=None, tags=None):
        """
        Create a new volume.

        Parameters
        ----------
        name : str
            The name of the new volume.
        region : str
            The slug identifier for the region where the volume should be created.
        size_gigabytes : int
            The size of the block storage volume in gigabytes.
        description : str, optional
            Optional text for the description of the volume.
        snapshot_id : str, optioal
            The unique identifier for the volume snapshot from which to create the volume.
        filesystem_type : str, optional
            The name of the filesystem type to be used on the volume. When provided, 
            the volume will automatically be formatted to the specified filesystem type.
        filesystem_label : str, optional
            The label to be applied to the filesystem.
        tags : list, optional
            List of tag names for the volume.

        Returns
        -------
        digitaloceanclient.models.Volume
        """

        payload = {
            'name': name,
            'region': region,
            'size_gigabytes': size_gigabytes,
        }
        if description:
            payload['description'] = description
        if snapshot_id:
            payload['snapshot_id'] = snapshot_id
        if filesystem_type:
            payload['filesystem_type'] = filesystem_type
        if filesystem_label:
            payload['filesystem_label'] = filesystem_label
        if tags:
            payload['tags'] = tags

        return super().create(payload=payload)

    def delete(self, volume_id):
        """
        Delete a volume.

        Parameters
        ----------
        volume_id : str
            The ID of the volume to be deleted.
        """
        return super().delete(volume_id)

    def create_snapshot(self, volume_id, name, tags=None):
        """
        Create snapshot from a volume.

        Parameters
        ----------
        volume_id : str
            The ID of the volume to create the snapshot from.
        name : str
            The name for the snapshot.
        tags : list, optional
            List of tag names from the snapshot.

        Returns
        -------
        digitaloceanclient.models.Snapshot

        Raises
        ------
        digitaloceanclient.exceptions.MalformedResponse
        """

        payload = {'name': name}
        response = self._request('POST', f'volumes/{volume_id}/snapshots', payload=payload)
        try:
            return Snapshot(response['snapshot'])
        except (KeyError, TypeError, ValueError):
            raise MalformedResponse('Invalid JSON for snapshot.')

    def update(self, *args, **kwargs):
        raise NotImplementedError
