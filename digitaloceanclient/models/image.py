from . import Model


class Image(Model):
    TYPE_SNAPSHOT = 'snapshot'
    TYPE_BACKUP = 'backup'
    TYPE_CUSTOM = 'custom'

    STATUS_NEW = 'NEW'
    STATUS_AVAILABLE = 'available'
    STATUS_PENDING = 'pending'
    STATUS_DELETED = 'deleted'

    # The identifier for the Image
    id = ''

    # The display name for the Image
    name = ''

    # Describes the kind of image. It may be one of 
    # "snapshot", "backup", or "custom"
    type = ''

    # Describes the base distribution used for this image
    distribution = ''

    # A uniquely identifying string that is associated with each of the 
    # DigitalOcean-provided public images
    slug = ''

    # Whether this image is public or not
    public = False

    # An array of the regions that the image is available in
    regions = []

    # The time value given in ISO8601
    created_at = ''

    # The minimum disk size in GB required for a Droplet to use this image
    min_disk_size = 0

    # The size of the image in gigabytes
    size_gigabytes = 0

    # An optional free-form text field to describe an image
    description = ''

    # An array containing the names of the tags the image has been tagged with.
    tags = []

    # A status string indicating the state of a custom image. 
    # This may be "NEW", "available", "pending", or "deleted"
    status = ''

    # A string containing information about errors that may occur 
    # when importing a custom image
    error_message = ''

    def __str__(self):
        return f'{self.distribution} {self.name}'
