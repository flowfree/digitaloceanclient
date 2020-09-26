from . import Model 


class Kernel(Model):
    """
    Represents a kernel resource.

    Attributes
    ----------
    id : str
        Kernel unique identifier.
    name : str
        The display name of the Kernel.
    version : str
        Kernel version
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        self.id = ''
        self.name = ''
        self.version = ''

        super().__init__(data)
