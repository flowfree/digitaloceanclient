import os

from digitaloceanclient import DigitalOceanClient
from digitaloceanclient.models import Image

access_token = os.getenv('ACCESS_TOKEN')
droplet_id = os.getenv('DROPLET_ID')

do = DigitalOceanClient(access_token)
try:
    print(f'Deleting droplet {droplet_id}...', end='')
    do.droplets.delete(droplet_id)
    print('done.')
except do.APIError as e:
    print(e)
