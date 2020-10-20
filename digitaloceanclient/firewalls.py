from .http_client import HttpClient
from .models import Firewall


class Firewalls(HttpClient):
    """
    Create, retrieve, update, and delete Firewalls.
    """

    model = Firewall

    def all(self):
        """
        List all Firewalls.

        Yields
        ------
        digitaloceanclient.models.Firewall

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().all()

    def create(self, name, inbound_rules, outbound_rules, 
               droplet_ids=None, tags=None):
        """
        Create a new Firewall.

        Parameters
        ----------
        name : str
            The name of the Firewall.
        inbound_rules : list of dict
            Dictionaries specifying the inbound rules for the Firewall.
        outbound_rules : list of dict
            Dictionaries specifying the outbound rules for the Firewall.
        droplet_ids : list, optional
            List of droplet IDs to be assigned to the Firewall.
        tags : list, optional
            List of tags to be assigned to the Firewall.

        Returns
        -------
        digitaloceanclient.models.Firewall

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'name': name,
            'inbound_rules': inbound_rules,
            'outbound_rules': outbound_rules,
        }
        if droplet_ids:
            payload['droplet_ids'] = droplet_ids

        return super().create(payload=payload)

    def get(self, firewall_id):
        """
        Retrieve an existing Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall to retrieve.

        Returns
        -------
        digitaloceanclient.models.Firewall

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().get(resource_id=firewall_id)

    def update(self, name, firewall_id, inbound_rules, outbound_rules,
                     droplet_ids=None, tags=None):
        """
        Update a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall to be updated.
        name : str
            The name of the Firewall.
        inbound_rules : list of dict
            Dictionaries specifying the inbound rules for the Firewall.
        outbound_rules : list of dict
            Dictionaries specifying the outbound rules for the Firewall.
        droplet_ids : list, optional
            List of droplet IDs to be assigned to the Firewall.
        tags : list, optional
            List of tags to be assigned to the Firewall.

        Returns
        -------
        digitaloceanclient.models.Firewall

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'name': name,
            'inbound_rules': inbound_rules,
            'outbound_rules': outbound_rules,
        }
        if droplet_ids:
            payload['droplet_ids'] = droplet_ids

        return super().update(resource_id=firewall_id, payload=payload)

    def delete(self, firewall_id):
        """
        Delete a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall to retrieve.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().delete(resource_id=firewall_id)

    def add_droplets(self, firewall_id, droplet_ids):
        """
        Assign Droplets to a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall.
        droplet_ids : list
            List of Droplet IDs to be assigned to the Firewall.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'firewalls/{firewall_id}/droplets'
        payload = {'droplet_ids': droplet_ids}
        return self._request('POST', path=path, payload=payload)

    def remove_droplets(self, firewall_id, droplet_ids):
        """
        Remove Droplets from a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall.
        droplet_ids : list
            List of Droplet IDs to be removed from the Firewall.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'firewalls/{firewall_id}/droplets'
        payload = {'droplet_ids': droplet_ids}
        return self._request('DELETE', path=path, payload=payload)

    def add_tags(self, firewall_id, tags):
        """
        Assign tags to a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall.
        tags : list
            List of tags to be assigned to the Firewall.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'firewalls/{firewall_id}/tags'
        payload = {'tags': tags}
        return self._request('POST', path=path, payload=payload)

    def remove_tags(self, firewall_id, tags):
        """
        Remove tags from a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall.
        tags : list
            List of tags to be assigned to the Firewall.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'firewalls/{firewall_id}/tags'
        payload = {'tags': tags}
        return self._request('DELETE', path=path, payload=payload)

    def add_rules(self, firewall_id, inbound_rules=None, outbound_rules=None):
        """
        Add additional access rules to a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall.
        inbound_rules : list of dict, optional
            Dictionaries of the inbound rules for the Firewall.
        outbound_rules : list of dict, optional
            Dictionaries of the outbound rules for the Firewall.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        if inbound_rules is None and outbound_rules is None:
            raise ValueError('Please specify inbound_rules or outbound_rules.')
        payload = {}
        if inbound_rules:
            payload['inbound_rules'] = inbound_rules
        if outbound_rules:
            payload['outbound_rules'] = outbound_rules
        path = f'firewalls/{firewall_id}/rules'
        return self._request('POST', path=path, payload=payload)

    def remove_rules(self, firewall_id, inbound_rules=None, outbound_rules=None):
        """
        Remove existing access rules from a Firewall.

        Parameters
        ----------
        firewall_id : str
            The ID of the Firewall.
        inbound_rules : list of dict, optional
            Dictionaries of the inbound rules to be removed from the Firewall.
        outbound_rules : list of dict, optional
            Dictionaries of the outbound rules to be removed from the Firewall.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        if inbound_rules is None and outbound_rules is None:
            raise ValueError('Please specify inbound_rules or outbound_rules.')
        payload = {}
        if inbound_rules:
            payload['inbound_rules'] = inbound_rules
        if outbound_rules:
            payload['outbound_rules'] = outbound_rules
        path = f'firewalls/{firewall_id}/rules'
        return self._request('DELETE', path=path, payload=payload)
