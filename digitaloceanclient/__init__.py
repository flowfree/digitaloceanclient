from .droplets import Droplets 


class DigitalOceanClient(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.droplets = Droplets(access_token)
