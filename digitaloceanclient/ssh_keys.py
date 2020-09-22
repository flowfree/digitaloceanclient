from .http_client import HttpClient
from .models import SSHKey
from .exceptions import MalformedResponse


class SSHKeys(HttpClient):
    model = SSHKey

    def all(self):
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
        return self._request('GET', f'account/keys/{key_id_or_fingerprint}')

    def create(self, name, public_key):
        payload = dict(name=name, public_key=public_key)
        return self._request('POST', f'account/keys', payload=payload)

    def update(self, key_id_or_fingerprint, name):
        payload = dict(name=name)
        return self._request('PUT', f'account/keys/{key_id_or_fingerprint}', payload=payload)

    def delete(self, key_id_or_fingerprint):
        return self._request('DELETE', f'account/keys/{key_id_or_fingerprint}')

    def _request(self, *args, **kwargs):
        response = super()._request(*args, **kwargs)
        if response:
            try:
                return self.model(response['ssh_key'])
            except (KeyError, TypeError):
                raise MalformedResponse('Invalid JSON response')
