import json 


class Model(object):
    def __init__(self, data):
        if type(data) != dict:
            data = json.loads(data)
        for key, val in data.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def __str__(self):
        if hasattr(self, 'slug'):
            return self.slug
        elif hasattr(self, 'name'):
            return self.name
        elif hasattr(self, 'uuid'):
            return self.uuid
        else:
            class_name = self.__class__.__name__
            return f'{class_name} Instance'


from .account import Account
from .action import Action
from .balance import Balance
from .billing_history import BillingHistory
from .cdn_endpoint import CDNEndpoint
from .certificate import Certificate
from .database import Database
from .domain import Domain
from .domain_record import DomainRecord
from .droplet import Droplet
from .droplet_action import DropletAction
from .floating_ip import FloatingIP
from .floating_ip_action import FloatingIPAction
from .image import Image
from .kernel import Kernel
from .region import Region
from .size import Size
from .volume import Volume
