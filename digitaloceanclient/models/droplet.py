from . import Model
from .kernel import Kernel
from .image import Image
from .region import Region


class Droplet(Model):
    """
    Represents a Droplet resource.

    Attributes
    ----------
    id : str
        Automatically generated unique identifier for the droplet instance
    name : str
        Human readable name set for the droplet instance
    memory : int
        Memory of the droplet in megabytes
    vcpus : int
        The number of virtual CPUs
    disk : int
        The size of the disk in gigabytes
    locked : bool
        Whether the Droplet has been locked, preventing actions by users.
    created_at : str
        When the droplet was created.
    status : str
        Status of the droplet instance. Valid values: new, active, off, archive
    backup_ids : list
        Array of backup IDs that have been taken of the Droplet instance.
    snapshot_ids : list
        An array of snapshot IDs of any snapshots created from the Droplet instance.
    features : list
        An array of features enabled on this Droplet.
    region : digitaloceanclient.models.Region
        The region that the Droplet instance is deployed in
    image : digitaloceanclient.models.Image
        The base image used to create the Droplet instance
    size : digitaloceanclient.models.Size
        The size object describing the droplet
    size_slug : ''
        The unique slug identifier for the size of this Droplet.
    networks : dict
        The details of the network that are configured for the Droplet instance. 
        This is an object that contains keys for IPv4 and IPv6.
    kernel : digitaloceanclient.models.Kernel
        The current kernel. This will initially be set to the kernel of the base 
        image when the Droplet is created.
    tags : list
        An array of Tags the Droplet has been tagged with.
    volume_ids : list
        A flat array including the unique identifier for each Block Storage volume 
        attached to the Droplet.
    vpc_uuid : str
        A string specifying the UUID of the VPC to which the Droplet is assigned.
    """

    STATUS_NEW = 'new'
    STATUS_ACTIVE = 'active'
    STATUS_OFF = 'off'
    STATUS_ARCHIVE = 'archive'

    id = None
    name = ''
    memory = 0
    vcpus = 0
    disk = 0
    locked = False
    created_at = ''
    status = ''
    backup_ids = []
    snapshot_ids = []
    features = []
    region = None
    image = None
    size = None
    size_slug = ''
    networks = None
    kernel = None
    tags = []
    volume_ids = []
    vpc_uuid = ''

    def __init__(self, data):
        super().__init__(data)
        classes = {'kernel': Kernel, 'image': Image, 'region': Region}
        for attrib, class_ in classes.items():
            try:
                setattr(self, attrib, class_(data[attrib]))
            except (KeyError, TypeError):
                setattr(self, attrib, None)
