from .model import Model
from .kernel import Kernel
from .image import Image
from .region import Region
from .networks import Networks


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
    networks : digitaloceanclient.models.Networks
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
    public_ip_address : str
        The first item in Droplet.networks.v4 where type='public'
    """

    STATUS_NEW = 'new'
    STATUS_ACTIVE = 'active'
    STATUS_OFF = 'off'
    STATUS_ARCHIVE = 'archive'

    @property
    def public_ip_address(self):
        if self.networks.v4:
            for item in self.networks.v4:
                if item.type == 'public':
                    return item.ip_address

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = None
        self.name = ''
        self.memory = 0
        self.vcpus = 0
        self.disk = 0
        self.locked = False
        self.created_at = ''
        self.status = ''
        self.backup_ids = []
        self.snapshot_ids = []
        self.features = []
        self.region = None
        self.image = None
        self.size = None
        self.size_slug = ''
        self.networks = None
        self.kernel = None
        self.tags = []
        self.volume_ids = []
        self.vpc_uuid = ''

        super().__init__(data)

        classes = {'kernel': Kernel, 
                   'image': Image, 
                   'region': Region,
                   'networks': Networks}
        for attrib, class_ in classes.items():
            try:
                setattr(self, attrib, class_(data[attrib]))
            except (KeyError, TypeError):
                setattr(self, attrib, None)
