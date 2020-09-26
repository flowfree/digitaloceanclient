from pathlib import Path 
import time
import os
import sys

from digitaloceanclient import DigitalOceanClient


# The hardcoded parameters for the Droplet
# To get the list of images, sizes, and regions, see the `create_new_droplet.py` file.
DROPLET_NAME = 'test-droplet'
DROPLET_IMAGE = 'ubuntu-20-04-x64'
DROPLET_SIZE = 's-1vcpu-1gb'
DROPLET_REGION = 'nyc1'

try:
    public_key_filename = Path.home() / '.ssh/id_rsa.pub'
    with open(public_key_filename) as f:
        public_key = f.read()
except FileNotFoundError:
    print('Cannot find the public key file.')
    sys.exit()

access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)

# Upload the public key
try:
    ssh_key = do.ssh_keys.create(name='my-ssh-key', public_key=public_key)
    print(f'Added new key: {ssh_key}')
except do.APIError as e:
    print(f'Failed creating new key: {e}')
    sys.exit(1)

# Create new Droplet with the SSH key embedded
try:
    print('\nCreating droplet...', end='')
    droplet, action = do.droplets.create(name=DROPLET_NAME,
                                         image=DROPLET_IMAGE,
                                         size=DROPLET_SIZE,
                                         region=DROPLET_REGION,
                                         ssh_keys=[ssh_key.id])
    while True:
        do.actions.refresh(action)
        if action.is_in_progress():
            time.sleep(2)
            continue
        elif action.is_completed():
            print(f'done.')
            break
        elif action.is_errored():
            print(f'failed.')
            break
except do.APIError as e:
    print(e)
    sys.exit(1)

# Get the detail of the newly created droplet
try:
    droplet = do.droplets.get(droplet.id)
    print(f'IP address = {droplet.public_ip_address}')
except do.APIError as e:
    print(e)
