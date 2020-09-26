from . import Model


class Domain(Model):
    """
    Represents a Domain resource.

    Attributes
    ----------
    name : str
        Name of the domain.
    ttl : int
        Time to live for the records in this domain in seconds.
    zone_file : str
        Complete contents of the zone file.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.name = ''
        self.ttl = 0
        self.zone_file = ''

        super().__init__(data)
