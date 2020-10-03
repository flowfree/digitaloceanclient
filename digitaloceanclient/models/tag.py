from .model import Model


class Tag(Model):
    """
    Represents a label that can be applied to a resource.

    Attributes
    ----------
    name : str
        The name of the tag.
    resources : Tag.Resources
        Embedded object containing key value pairs of resource types
        and resource statistics.
    """

    class Resources(Model):

        class Item(Model):
            count = 0
            last_tagged_uri = None

        def __init__(self, data):
            self.count = 0
            self.last_tagged_uri = None
            self.droplets = None
            self.images = None
            self.volumes = None
            self.volume_snapshots = None
            self.databases = None

            super().__init__(data)

            for attrib in ['droplets', 'images', 'volumes',
                           'volume_snapshots', 'databases']:
                try:
                    setattr(self, attrib, Tag.Resources.Item(data[attrib]))
                except (KeyError, ValueError):
                    pass

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.name = None
        self.resources = None

        super().__init__(data)

        try:
            self.resources = Tag.Resources(data['resources'])
        except (KeyError, ValueError):
            pass
