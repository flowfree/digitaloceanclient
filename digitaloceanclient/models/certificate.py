from . import Model 


class Certificate(Model):
    """
    Represents a Certificate.

    Attributes
    ----------
    id : str
        Unique identifier for the certificate.
    name : str
        Human-readable name for the certificate.
    not_after : str
        Expiration date
    sha1_fingerprint : str
        A unique identifier generated from the SHA-1 fingerprint 
        of the certificate.
    created_at : str
        When the Certificate was created.
    dns_names : list
        An array of fully qualified domain names (FQDNs) for which 
        the certificate was issued.
    state : str
        A string representing the current state of the certificate 
        It may be "pending", "verified", or "error".
    type : str
        A string representing the type of the certificate
        The value will be "custom" for a user-uploaded certificate or 
        "lets_encrypt" for one automatically generated with Let's Encrypt.
    """

    STATE_PENDING = 'pending'
    STATE_VERIFIED = 'verified'
    STATE_ERROR = 'error'

    TYPE_CUSTOM = 'custom'
    TYPE_LETS_ENCRYPT = 'lets_encrypt'

    id = ''
    name = ''
    not_after = ''
    sha1_fingerprint = ''
    created_at = ''
    dns_names = []
    state = ''
    type = ''
