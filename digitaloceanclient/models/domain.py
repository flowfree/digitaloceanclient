from . import Model


class Domain(Model):
    # Name of the domain
    name = ''

    # Time to live for the records in this domain in seconds
    ttl = 0

    # Complete contents of the zone file
    zone_file = ''
