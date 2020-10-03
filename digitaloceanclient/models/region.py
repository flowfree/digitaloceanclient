from .model import Model


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

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.slug = ''
        self.name = ''
        self.sizes = []
        self.available = False
        self.features = []

        super().__init__(data)

    def __str__(self):
        return self.name
