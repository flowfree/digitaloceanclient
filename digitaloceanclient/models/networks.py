from . import Model


class Networks(Model):
    """
    Represents the networks for a Droplet.

    Attributes
    ----------
    v4 : list
    v6 : list
    """


    class NetworkItem(Model):
        def __init__(self, data):
            self.ip_address = ''
            self.netmask = ''
            self.gateway = ''
            self.type = ''
            super().__init__(data)

        def __str__(self):
            return self.ip_address


    def __init__(self, data):
        """
        Parameters
        ----------
        data : dict
            The JSON response from the API.
        """

        super().__init__(data)

        try:
            self.v4 = [Networks.NetworkItem(x) for x in data['v4']]
            self.v6 = [Networks.NetworkItem(x) for x in data['v6']]
        except (KeyError, TypeError):
            pass
