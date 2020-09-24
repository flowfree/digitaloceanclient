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

    id = ''
    name = ''
    version = ''
