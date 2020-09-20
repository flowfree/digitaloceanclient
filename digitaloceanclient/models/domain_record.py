from . import Model


class DomainRecord(Model):
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

    # Unique identifier
    id = ''

    # The type of the DNS record
    type = ''

    # The host name, alias, or service being defined by the record
    name = ''

    # Variable data depending on record type
    data = ''

    # The priority for SRV and MX records
    priority = None

    # The port for SRV records
    port = None

    # time to live for the record, in seconds
    ttl = 0

    # The weight for SRV records
    weight = None

    # An unsigned integer between 0-255 used for CAA records
    flags = None

    # The parameter tag for CAA records
    # Valid values are "issue", "issuewild", or "iodef"
    tag = None
