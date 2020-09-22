import os

from digitaloceanclient import DigitalOceanClient 


access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)
try:
    for ssh_key in do.ssh_keys.all():
        print(f'ID = {ssh_key.id}, Name = {ssh_key.name}')
except do.APIError as e:
    print(e)
