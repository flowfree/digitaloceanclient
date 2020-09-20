from . import Model 
from .droplet import Droplet
from .region import Region


class FloatingIP(Model):
    # The public IP address
    ip = ''

    # The droplet that the floating IP has been assigned to
    droplet = None

    # The region that the floating IP is reserved to
    region = None

    def __init__(self, data):
        super().__init__(data)
        try:
            self.droplet = Droplet(data['droplet'])
        except (KeyError, TypeError):
            pass
        try:
            self.region = Region(data['region'])
        except (KeyError, TypeError):
            pass
