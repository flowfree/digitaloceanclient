from pathlib import Path
import os
import sys

from digitaloceanclient import DigitalOceanClient


try:
    ssh_filename = Path.home() / '.ssh/id_rsa.pub'
    with open(ssh_filename) as f:
        public_key = f.read()
except FileNotFoundError:
    print(f'Cannot find the id_rsa.pub file.')
    sys.exit(1)

access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)

try:
    ssh_key = do.ssh_keys.create(name='test-ssh-key', public_key=public_key)
    print(f'Successfully added new key: {ssh_key}')
except do.APIError as e:
    print(e)
