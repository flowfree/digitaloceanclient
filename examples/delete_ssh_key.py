import os
import sys

from digitaloceanclient import DigitalOceanClient 


access_token = os.getenv('ACCESS_TOKEN')
ssh_key_id = os.getenv('SSH_KEY_ID')
do = DigitalOceanClient(access_token)

try:
    do.ssh_keys.delete(ssh_key_id)
except do.APIError as e:
    print(e)
    sys.exit(1)

try:
    ssh_key = do.ssh_keys.get(ssh_key_id)
    print('Alert! SSH key still exist!')
except do.NotFound:
    print('SSH key removed.')
