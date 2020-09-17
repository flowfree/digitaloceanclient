import json 

import jsonpickle


class Region(object):
    # The Region unique identifier
    slug = ''

    # The display name of the Region
    name = ''

    # An array which contains the identifying slugs for the sizes 
    # available in this region
    sizes = []

    # Whether new Droplets can be created in this region
    available = False

    # An array which contains features available in this region
    features = []

    @staticmethod
    def from_json(d):
        if type(d) != dict:
            d = json.loads(d)
        d['py/object'] = 'digitaloceanclient.models.Region'
        return jsonpickle.decode(json.dumps(d))

    def __str__(self):
        return self.name
