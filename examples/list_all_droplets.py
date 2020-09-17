import os
from digitaloceanclient import DigitalOceanClient

"""
List all of your droplets.
"""

access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)

for droplet in do.droplets.all():
    print(f'ID = {droplet.id}')
    print(f'Name = {droplet.name}')
    print(f'Memory = {droplet.memory} MB')
    print(f'Image = {droplet.image.name}')
    print(f'Region = {droplet.region.name}')
    print(f'Created at = {droplet.created_at}')
