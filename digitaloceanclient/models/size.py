from . import Model


class Size(Model):
    # Human-readable string as the identifier of the Size
    slug = ''

    # Whether Droplet can be created with this Size
    memory = 0

    # The integer of number CPUs allocated to Droplets of this size
    vcpus = 0

    # The amount of disk space set aside for Droplets of this size
    # in gigabytes
    disk = 0

    # The amount of transfer bandwidth that is available for Droplets 
    # created in this size in terabytes
    transfer = 0

    # Monthly cost of this Droplet size in USD
    price_monthly = 0

    # Hourly cost of this Droplet size in USD 
    price_hourly = 0

    # An array containing the region slugs where this size is available for Droplet creates
    regions = []

    # Whether new Droplets can be created with this size
    available = False
