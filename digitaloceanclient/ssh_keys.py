from .http_client import HttpClient
from .models import SSHKey
from .exceptions import MalformedResponse


class SSHKeys(HttpClient):
    model = SSHKey

    def all(self):
        next_url = 'account/keys'
        while True:
            response = self._request('GET', next_url)
            for row in response.get('ssh_keys', []):
                yield self.model(row)
            try:
                next_url = response['links']['pages']['next']
            except KeyError:
                break

    def get(self, key_id_or_fingerprint):
        response = self._request('GET', f'account/keys/{key_id_or_fingerprint}')
        try:
            return self.model(response['ssh_key'])
        except (KeyError, TypeError):
            raise MalformedResponse('Invalid JSON response')
