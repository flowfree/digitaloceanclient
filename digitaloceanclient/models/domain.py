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

    name = ''
    ttl = 0
    zone_file = ''
