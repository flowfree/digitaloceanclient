from .model import Model


class Size(Model):
    """
    Represents the Size object.

    Attributes
    ----------
    slug : str
        Human-readable string as the identifier of the Size
    memory : int
        The amount of RAM in megabytes
    vcpus : int
        The number of CPUs allocated to Droplets of this size
    disk : int
        The amount of disk space set aside for Droplets of this
        size in gigabytes
    transfer : float
        The amount of transfer bandwidth that is available for Droplets
        created in this size in terabytes
    price_monthly : float
        Monthly cost of this Droplet size in USD
    price_hourly : float
        Hourly cost of this Droplet size in USD
    regions : list
        An array containing the region slugs where this size is
        available for Droplet creates
    available : bool
        Whether new Droplets can be created with this size
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.slug = ''
        self.memory = 0
        self.vcpus = 0
        self.disk = 0
        self.transfer = 0
        self.price_monthly = 0
        self.price_hourly = 0
        self.regions = []
        self.available = False

        super().__init__(data)

    def __str__(self):
        return (f'Monthly price=${self.price_monthly}, '
                f'CPU={self.vcpus}, Memory={self.memory} MB, '
                f'Disk={self.disk} GB, Transfer={self.transfer} TB')
