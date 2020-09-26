from . import Model


class DomainRecord(Model):
    """
    Represents individual DNS record configured for a domain.

    Attributes
    ----------
    id : str
        Unique identifier for the domain record.
    type : str
        The type of the DNS record.
    name : str
        The host name, alias, or service being defined by the record.
    data : str
        Variable data depending on record type.
    priority : int
        The priority for SRV and MX records.
    port : int
        The port for SRV records.
    ttl : int
        Time to live for the record, in seconds.
    weight : int
        The weight for SRV records.
    flags : int
        An unsigned integer between 0-255 used for CAA records.
    tag : str
        The parameter tag for CAA records
        Valid values are "issue", "issuewild", or "iodef"
    """

    TYPE_A = 'A'
    TYPE_AAAA = 'AAAA'
    TYPE_CAA = 'CAA'
    TYPE_CNAME = 'CNAME'
    TYPE_MX = 'MX'
    TYPE_NS = 'NS'
    TYPE_TXT = 'TXT'
    TYPE_SRV = 'SRV'
    TYPE_SOA = 'SOA'

    TAG_ISSUE = 'issue'
    TAG_ISSUEWILD = 'issuewild'
    TAG_IODEF = 'iodef'

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = ''
        self.type = ''
        self.name = ''
        self.data = ''
        self.priority = None
        self.port = None
        self.ttl = 0
        self.weight = None
        self.flags = None
        self.tag = None

        super().__init__(data)
