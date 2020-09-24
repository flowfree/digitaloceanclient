from .http_client import HttpClient
from .models import Action, Droplet
from .exceptions import MalformedResponse


class Droplets(HttpClient):
    """
    Create, list, update, and delete Droplets.
    """

    model = Droplet

    def get(self, droplet_id):
        """
        Retrieve a single Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the droplet to retrieve.

        Returns
        -------
        digitaloceanclient.models.Droplet
        """

        response = self._request('GET', f'droplets/{droplet_id}')
        data = response.get('droplet', {})
        return self.model(data)

    def create(self, name, image, size, region, ssh_keys=None, backups=False,
               ipv6=True, private_networking=False, vpc_uuid=None, user_data=None,
               monitoring=False, volumes=None, tags=None):
        """
        Create a new Droplet.

        Parameters
        ----------
        name : str
            The name of the Droplet to create.
        image : str or int
            The image ID of a public or private image, or the unique slug
            for a public image.
        size : str
            The slug identifier for the size of the Droplet.
        region : str
            The slug identifier for the region where the Droplet to deploy in. 
        ssh_keys : list, optional
            List of the IDs or fingerprints SSH keys to embed upon creation.
        backups : bool, optional
            Whether automated backups should be enabled.
        ipv6 : bool, optional
            Whether IPv6 should be enabled.
        private_networking : bool, optional
            Whether private networking should be enabled.
        vpc_uuid : str, optional
            The UUID of the VPC to which the Droplet will be assigned.
        user_data : str, optional
            Custom data which may be used to configure the Droplet on first boot, 
            e.g: bash script
        monitoring : bool, optional
            Whether to install the DigitalOcean agent for monitoring.
        volumes : list, optional
            List of unique string identifier for each block storage volume to be 
            attached to the Droplet.
        tags : list, optional
            List of tags for the Droplet.

        Returns
        -------
        digitaloceanclient.models.Droplet
            The Droplet in creation.
        digitaloceanclient.models.Action
            For checking the status of the Droplet create event.

        Raises
        ------
        digitaloceanclient.exceptions.MalformedResponse
            When the JSON response cannot be populated to the Droplet model.
        digitaloceanclient.exceptions.APIError
            For various HTTP errors.
        """

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

        try:
            droplet = self.model(response['droplet'])
            action = Action({'id': response['links']['actions'][0]['id']})
        except (KeyError, TypeError, IndexError):
            raise MalformedResponse('Invalid JSON response.')

        return droplet, action

    def delete(self, droplet_id):
        """
        Delete a Droplet.

        Parameters
        ----------
        droplet_id : str
            The ID of the Droplet to be deleted.
        """

        self._request('DELETE', f'droplets/{droplet_id}')
