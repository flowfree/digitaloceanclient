from .account import Account
from .droplets import Droplets 
from .images import Images
from .regions import Regions
from .sizes import Sizes
from .exceptions import Unauthorized


class DigitalOceanClient(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.account = Account(access_token)
        self.droplets = Droplets(access_token)
        self.images = Images(access_token)
        self.regions = Regions(access_token)
        self.sizes = Sizes(access_token)

        self.Unauthorized = Unauthorized

