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
from .droplet import Droplet
from .image import Image
from .kernel import Kernel
from .region import Region
from .size import Size
