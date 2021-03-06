from .model import Model


class CDNEndpoint(Model):
    """
    Represents a CDN endpoint hosted in DigitalOcean.

    Attributes
    ----------
    id : str
        Unique identifier for the CDN endpoint.
    origin : str
        The fully qualified domain name (FQDN) for the origin server 
        which the provides the content for the CDN.
    endpoint : str
        The fully qualified domain name (FQDN) from which the CDN-backed.
        content is served
    created_at : str
        A time value given in ISO8601 combined date and time format.
    certificate_id : str
        The ID of a DigitalOcean managed TLS certificate used for SSL when 
        a custom subdomain is provided.
    custom_domain : str
        The fully qualified domain name (FQDN) of the custom subdomain 
        used with the CDN Endpoint.
    ttl : int
        The amount of time the content is cached by the CDN's edge servers in seconds.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = ''
        self.origin = ''
        self.endpoint = ''
        self.created_at = ''
        self.certificate_id = ''
        self.custom_domain = ''
        self.ttl = 0

        super().__init__(data)
