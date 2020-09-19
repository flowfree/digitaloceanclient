from . import Model


class Account(Model):
    STATUS_ACTIVE = 'active'
    STATUS_WARNING = 'warning'
    STATUS_LOCKED = 'locked'

    # The unique universal identifier for the current user
    uuid = ''

    # Total number of Droplets the current user or team may have at one time
    droplet_limit = 0

    # Total number of floating IPs the current user or team may have
    floating_ip_limit = 0

    # Total number of volumes the current user or team may have
    volume_limit = 0

    # The email address used by the current user
    email = ''

    # Whether the user has verified their email address
    email_verified = False

    # This value is one of "active", "warning" or "locked"
    status = ''

    # A human-readable message giving more details about the status of the account
    status_message = ''
