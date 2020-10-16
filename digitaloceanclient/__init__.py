from .account import Account
from .actions import Actions
from .cdn_endpoints import CDNEndpoints
from .certificates import Certificates
from .domains import Domains
from .domain_records import DomainRecords
from .droplets import Droplets 
from .droplet_actions import DropletActions
from .exceptions import (
    APIError, BadRequest, MalformedResponse, NotFound, RateLimitExceeded, 
    ServerError, Unauthorized, UnprocessableEntity
)
from .floating_ips import FloatingIPs
from .floating_ip_actions import FloatingIPActions
from .images import Images
from .regions import Regions
from .sizes import Sizes
from .snapshots import Snapshots
from .ssh_keys import SSHKeys
from .tags import Tags
from .volumes import Volumes


class DigitalOceanClient(object):
    def __init__(self, access_token):
        self.access_token = access_token

        # Related objects
        self.account = Account(access_token)
        self.actions = Actions(access_token)
        self.cdn_endpoints = CDNEndpoints(access_token)
        self.certificates = Certificates(access_token)
        self.domains = Domains(access_token)
        self.domain_records = DomainRecords(access_token)
        self.droplets = Droplets(access_token)
        self.droplet_actions = DropletActions(access_token)
        self.floating_ips = FloatingIPs(access_token)
        self.floating_ip_actions = FloatingIPActions(access_token)
        self.images = Images(access_token)
        self.regions = Regions(access_token)
        self.sizes = Sizes(access_token)
        self.snapshots = Snapshots(access_token)
        self.ssh_keys = SSHKeys(access_token)
        self.tags = Tags(access_token)
        self.volumes = Volumes(access_token)

        # Exceptions
        self.APIError = APIError
        self.BadRequest = BadRequest
        self.MalformedResponse = MalformedResponse
        self.NotFound = NotFound
        self.RateLimitExceeded = RateLimitExceeded
        self.ServerError = ServerError
        self.Unauthorized = Unauthorized
        self.UnprocessableEntity = UnprocessableEntity
