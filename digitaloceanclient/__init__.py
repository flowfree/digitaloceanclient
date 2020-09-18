from .account import Account
from .droplets import Droplets 
from .exceptions import (
    NotFound, ServerError, Unauthorized
)
from .images import Images
from .regions import Regions
from .sizes import Sizes


class DigitalOceanClient(object):
    def __init__(self, access_token):
        self.access_token = access_token

        # Related objects
        self.account = Account(access_token)
        self.droplets = Droplets(access_token)
        self.images = Images(access_token)
        self.regions = Regions(access_token)
        self.sizes = Sizes(access_token)

        # Exceptions
        self.NotFound = NotFound
        self.ServerError = ServerError
        self.Unauthorized = Unauthorized

