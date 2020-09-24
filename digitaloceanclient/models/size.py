from . import Model


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
        The amount of disk space set aside for Droplets of this size in gigabytes
    transfer : float
        The amount of transfer bandwidth that is available for Droplets 
        created in this size in terabytes
    price_monthly : float
        Monthly cost of this Droplet size in USD
    price_hourly : float
        Hourly cost of this Droplet size in USD 
    regions : list
        An array containing the region slugs where this size is available for Droplet creates
    available : bool
        Whether new Droplets can be created with this size
    """

    slug = ''
    memory = 0
    vcpus = 0
    disk = 0
    transfer = 0
    price_monthly = 0
    price_hourly = 0
    regions = []
    available = False

    def __str__(self):
        return (f'Monthly price=${self.price_monthly}, ' 
                f'CPU={self.vcpus}, Memory={self.memory} MB, '
                f'Disk={self.disk} GB, Transfer={self.transfer} TB')
