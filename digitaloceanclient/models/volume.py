from . import Model
from .region import Region


class Volume(Model):
    # Unique identifier for the storage volume
    id = None

    # The region that the block storage volume is located in
    region = None

    # Array containing the IDs of the Droplets the volume is attached to
    droplet_ids = []

    # A human-readable name for the block storage volume
    name = ''

    # An optional free-form text field to describe a block storage volume
    description = ''

    # The size of the block storage volume in GiB (1024^3)
    size_gigabytes = 0

    # A time value given in ISO8601 combined date and time format that 
    # represents when the block storage volume was created
    created_at = ''

    # The type of filesystem currently in-use on the volume
    filesystem_type = ''

    # The label currently applied to the filesystem
    filesystem_label = ''

    # An array of tags the volume has been tagged with
    tags = []

    def __init__(self, data):
        super().__init__(data)
        try:
            self.region = Region(data['region'])
        except KeyError:
            self.region = None
