from . import Model 
from .droplet import Droplet
from .region import Region


class FloatingIP(Model):
    """
    Represent the Floating IP resource.

    Attributes
    ----------
    ip : str
        The public IP address
    droplet : digitaloceanclient.models.Droplet
        The droplet that the floating IP has been assigned to.
    region : digitaloceanclient.models.Region
        The region that the floating IP is reserved to.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.ip = ''
        self.droplet = None
        self.region = None

        super().__init__(data)

        try:
            self.droplet = Droplet(data['droplet'])
        except (KeyError, TypeError):
            pass
        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass
