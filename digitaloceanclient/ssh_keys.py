from .http_client import HttpClient
from .models import SSHKey
from .exceptions import MalformedResponse


class SSHKeys(HttpClient):
    model = SSHKey

    def all(self):
        """
        List all SSH keys.

        Yields
        ------
        digitaloceanclient.models.SSHKey
        """

        next_url = 'account/keys'
        while True:
            response = super()._request('GET', next_url)
            for row in response.get('ssh_keys', []):
                yield self.model(row)
            try:
                next_url = response['links']['pages']['next']
            except KeyError:
                break

    def get(self, key_id_or_fingerprint):
        """
        Get a single SSH Key.

        Parameters
        ----------
        key_id_or_fingerprint : str
            The ID or fingerprint of the SSH key.

        Returns
        -------
        digitaloceanclient.models.SSHKey
        """

        return self._request('GET', f'account/keys/{key_id_or_fingerprint}')

    def create(self, name, public_key):
        """
        Create new SSH Key.

        Parameters
        ----------
        name : str
            The display name for the key.
        public_key : str
            The entire public key string.

        Returns
        -------
        digitaloceanclient.models.SSHKey
        """

        payload = dict(name=name, public_key=public_key)
        return self._request('POST', f'account/keys', payload=payload)

    def update(self, key_id_or_fingerprint, name):
        """
        Update existing SSH Key.

        Parameters
        ----------
        key_id_or_fingerprint : str
            The ID or fingerprint of the SSH key.
        name : str
            The new name for the SSH key.

        Returns
        -------
        digitaloceanclient.models.SSHKey
        """

        payload = dict(name=name)
        return self._request('PUT', f'account/keys/{key_id_or_fingerprint}', payload=payload)

    def delete(self, key_id_or_fingerprint):
        """
        Delete an SSH key.

        Parameters
        ----------
        key_id_or_fingerprint : str
            The ID or fingerprint of the SSH key.
        """

        return self._request('DELETE', f'account/keys/{key_id_or_fingerprint}')

    def _request(self, *args, **kwargs):
        response = super()._request(*args, **kwargs)
        if response:
            try:
                return self.model(response['ssh_key'])
            except (KeyError, TypeError):
                raise MalformedResponse('Invalid JSON response')
