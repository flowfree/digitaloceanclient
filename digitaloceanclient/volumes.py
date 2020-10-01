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

