from .http_client import HttpClient
from .models import Action, Droplet


class Droplets(HttpClient):
    model = Droplet

    def get(self, droplet_id):
        response = self._request('GET', f'droplets/{droplet_id}')
        data = response.get('droplet', {})
        return self.model(data)

    def create(self, name, image, size, region, ssh_keys=None, backups=False,
               ipv6=True, private_networking=False, vpc_uuid=None, user_data=None,
               monitoring=False, volumes=None, tags=None):
        payload = {
            'name': name,
            'image': image,
            'size': size,
            'region': region,
            'ssh_keys': ssh_keys,
            'backups': backups,
            'ipv6': ipv6, 
            'private_networking': private_networking,
            'vpc_uuid': vpc_uuid,
            'user_data': user_data,
            'monitoring': monitoring,
            'volumes': volumes,
            'tags': tags,
        }
        response = self._request('POST', 'droplets', payload=payload)
        droplet_dict = response.get('droplet', {})
        try:
            action_dict = {'id': response['links']['actions'][0]['id']}
            action = Action(action_dict)
        except (KeyError, IndexError):
            action = None

        return self.model(droplet_dict), action
