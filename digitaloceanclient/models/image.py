from . import Model


class Image(Model):
    """
    Represents an image for creating a Droplet.

    Attributes
    ----------
    id : str
        The identifier for the Image
    name : str
        The display name for the Image
    type : str
        Describes the kind of image. It may be one of "snapshot", "backup", or "custom"
    distribution : str
        Describes the base distribution used for this image
    slug : str
        A uniquely identifying string that is associated with each of the 
        DigitalOcean-provided public images.
    public : bool
        Whether this image is public or not.
    regions : list
        List of the regions that the image is available in.
    created_at : str
        The time value given in ISO8601.
    min_disk_size : int
        The minimum disk size in GB required for a Droplet to use this image.
    size_gigabytes : float
        The size of the image in gigabytes.
    description : str
        An optional free-form text field to describe an image.
    tags : list
        An array containing the names of the tags the image has been tagged with.
    status : str
        A status string indicating the state of a custom image. 
        This may be "NEW", "available", "pending", or "deleted".
    error_message : str
        A string containing information about errors that may occur 
        when importing a custom image.
    """

    TYPE_SNAPSHOT = 'snapshot'
    TYPE_BACKUP = 'backup'
    TYPE_CUSTOM = 'custom'

    STATUS_NEW = 'NEW'
    STATUS_AVAILABLE = 'available'
    STATUS_PENDING = 'pending'
    STATUS_DELETED = 'deleted'

    id = ''
    name = ''
    type = ''
    distribution = ''
    slug = ''
    public = False
    regions = []
    created_at = ''
    min_disk_size = 0
    size_gigabytes = 0
    description = ''
    tags = []
    status = ''
    error_message = ''

    def __str__(self):
        return f'{self.distribution} {self.name}'
