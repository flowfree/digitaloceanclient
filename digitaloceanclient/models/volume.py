from .model import Model
from .region import Region


class Volume(Model):
    """
    Represents a block storage volume.

    Attributes
    ----------
    id : str
        Unique identifier for the storage volume.
    region : digitaloceanclient.models.Region
        The region that the block storage volume is located in.
    droplet_ids : list
        Array containing the IDs of the Droplets the volume is attached to.
    name : str
        A human-readable name for the block storage volume.
    description : str
        An optional free-form text field to describe a block storage volume.
    size_gigabytes : int
        The size of the block storage volume in GiB (1024^3).
    created_at : str
        A time value given in ISO8601 combined date and time format that
        represents when the block storage volume was created.
    filesystem_type : str
        The type of filesystem currently in-use on the volume.
    filesystem_label : str
        The label currently applied to the filesystem.
    tags : list
        An array of tags the volume has been tagged with.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = None
        self.region = None
        self.droplet_ids = []
        self.name = ''
        self.description = ''
        self.size_gigabytes = 0
        self.created_at = ''
        self.filesystem_type = ''
        self.filesystem_label = ''
        self.tags = []

        super().__init__(data)

        try:
            self.region = Region(data['region'])
        except KeyError:
            self.region = None
