from .droplets import Droplets 
from .regions import Regions


class DigitalOceanClient(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.droplets = Droplets(access_token)
        self.regions = Regions(access_token)

