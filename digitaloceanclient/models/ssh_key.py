from . import Model


class SSHKey(Model):
    # Unique identifier for the key
    id = ''

    # The fingerprint value that is generated from the public key
    fingerprint = ''

    # The entire public key string that was uploaded
    # This is what is embedded into the root user's authorized_keys file
    public_key = ''

    # The display name for the key
    name = ''
