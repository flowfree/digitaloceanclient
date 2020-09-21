from .http_client import HttpClient
from .models import SSHKey


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
