from .model import Model


class SSHKey(Model):
    """
    Represent an SSH public key.


    Attributes
    ----------
    id : str
        Unique identifier for the key.
    fingerprint : str
        The fingerprint value that is generated from the public key.
    public_key : str
        The entire public key string that was uploaded
        This is what is embedded into the root user's authorized_keys file.
    name : str
        The display name for the key.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = ''
        self.fingerprint = ''
        self.public_key = ''
        self.name = ''

        super().__init__(data)
