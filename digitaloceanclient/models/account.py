from . import Model


class Account(Model):
    """
    Represent the current user's account information.

    Attributes
    ----------
    uuid : str
        The unique universal identifier for the current user
    droplet_limit : int
        Total number of Droplets the current user or team may have at one time
    floating_ip_limit : int
        Total number of floating IPs the current user or team may have
    volume_limit : int
        Total number of volumes the current user or team may have
    email : str
        The email address used by the current user
    email_verified : bool
        Whether the user has verified their email address
    status : str
        The current user's status: "active", "warning", "locked"
    status_message : str
        A human-readable message giving more details about the status of the account
    """

    STATUS_ACTIVE = 'active'
    STATUS_WARNING = 'warning'
    STATUS_LOCKED = 'locked'

    uuid = ''
    droplet_limit = 0
    floating_ip_limit = 0
    volume_limit = 0
    email = ''
    email_verified = False
    status = ''
    status_message = ''
