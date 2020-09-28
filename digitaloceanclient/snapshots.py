from .http_client import HttpClient
from .models import Snapshot


class Snapshots(HttpClient):
    """
    Retrieve and delete snapshots.

    Methods
    -------
    all(resource_type=None)
        Retrieve all snapshots and optionally filter by resource type.
    get(snapshot_id)
        Retrieve a single snapshot.
    delete(snapshot_id)
        Delete snapshot with the given ID.
    """

    model = Snapshot

    def all(self, resource_type=None):
        """
        Retrieve all Snapshots.

        Parameters
        ----------
        resource_type : {'droplet', 'volume'}, optional
            Filter by the given resource type.

        Yields
        ------
        digitaloceanclient.models.Snapshot
        """

        if resource_type:
            if resource_type not in ['droplet', 'volume']:
                raise ValueError(f'Invalid resource type: {resource_type}')
            params = {'resource_type': resource_type}
        else:
            params = None
        return super().all(params=params)

    def create(self, *args, **kwargs):
        raise NotImplementedError
