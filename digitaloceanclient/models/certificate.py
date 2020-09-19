from . import Model 


class Certificate(Model):
    STATE_PENDING = 'pending'
    STATE_VERIFIED = 'verified'
    STATE_ERROR = 'error'

    TYPE_CUSTOM = 'custom'
    TYPE_LETS_ENCRYPT = 'lets_encrypt'

    # Unique identifier
    id = ''

    # Human-readable name for the Certificate
    name = ''

    # Expiration date
    not_after = ''

    # A unique identifier generated from the SHA-1 fingerprint 
    # of the certificate
    sha1_fingerprint = ''

    # When the Certificate was created
    created_at = ''

    # An array of fully qualified domain names (FQDNs) for which 
    # the certificate was issued
    dns_names = []

    # A string representing the current state of the certificate 
    # It may be "pending", "verified", or "error".
    state = ''

    # A string representing the type of the certificate
    # The value will be "custom" for a user-uploaded certificate or 
    # "lets_encrypt" for one automatically generated with Let's Encrypt.
    type = ''
