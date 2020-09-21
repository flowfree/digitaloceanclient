from . import Model


class Snapshot(Model):
    # Unique identifier 
    id = ''

    # Name of the snapshot
    name = ''

    # An array of the regions that the image is available in
    regions = []

    # When the snapshot was created
    created_at = ''

    # A unique identifier for the resource that the action is associated with
    resource_id = ''

    # The type of resource that the action is associated with
    resource_type = ''

    # The minimum size in GB required for a volume or Droplet to use this snapshot
    min_disk_size = 0

    # The billable size of the snapshot in gigabytes
    size_gigabytes = 0

    # Array of tags the snapshot has been tagged with
    tags = []
