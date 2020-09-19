from .http_client import HttpClient
from .models import Droplet


class Droplets(HttpClient):
    model = Droplet

    def get(self, droplet_id):
        response = self._request('GET', f'droplets/{droplet_id}')
        data = response.get('droplet', {})
        return self.model(data)

