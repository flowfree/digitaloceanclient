import json 


class Model(object):
    """
    This is the base class for all of the models.
    """

    def __init__(self, data):
        self.from_json(data)

    def from_json(self, data):
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
