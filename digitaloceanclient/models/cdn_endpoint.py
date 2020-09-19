from . import Model


class CDNEndpoint(Model):
    # Unique identifier
    id = ''

    # The fully qualified domain name (FQDN) for the origin server 
    # which the provides the content for the CDN
    origin = ''

    # The fully qualified domain name (FQDN) from which the CDN-backed 
    # content is served
    endpoint = ''

    # A time value given in ISO8601 combined date and time format
    created_at = ''

    # The ID of a DigitalOcean managed TLS certificate used for SSL 
    # when a custom subdomain is provided
    certificate_id = ''

    # The fully qualified domain name (FQDN) of the custom subdomain 
    # used with the CDN Endpoint
    custom_domain = ''

    # The amount of time the content is cached by the CDN's edge servers 
    # in seconds
    ttl = 0
