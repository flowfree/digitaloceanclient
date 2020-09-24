from . import Model


class Region(Model):
    """
    Represents a datacenter where droplets can be deployed and 
    images can be transferred.

    Attributes
    ----------
    slug : str
        The Region unique identifier
    name : str
        The display name of the Region
    sizes : list
        An array which contains the identifying slugs for the sizes 
        available in this region
    available : bool
        Whether new Droplets can be created in this region
    features : list
        An array which contains features available in this region
    """

    slug = ''
    name = ''
    sizes = []
    available = False
    features = []

    def __str__(self):
        return self.name
