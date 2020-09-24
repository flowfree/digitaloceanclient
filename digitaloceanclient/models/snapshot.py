from . import Model


class Snapshot(Model):
    """
    Represents a saved instance of a Droplet or a block storage volume.

    Attributes
    ----------
    id : str
        Unique identifier 
    name : str
        Name of the snapshot
    regions : list
        An array of the regions that the image is available in
    created_at : str
        When the snapshot was created
    resource_id : str
        A unique identifier for the resource that the action is associated with
    resource_type : str
        The type of resource that the action is associated with
    min_disk_size : int
        The minimum size in GB required for a volume or Droplet to use this snapshot
    size_gigabytes : float
        The billable size of the snapshot in gigabytes
    tags : list
        Array of tags the snapshot has been tagged with
    """

    id = ''
    name = ''
    regions = []
    created_at = ''
    resource_id = ''
    resource_type = ''
    min_disk_size = 0
    size_gigabytes = 0
    tags = []
