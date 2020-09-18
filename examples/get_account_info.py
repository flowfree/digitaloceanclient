import os
from digitaloceanclient import DigitalOceanClient

"""
Get current user's account information.
"""

access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)
account = do.account.get()
print(f'UUID = {account.uuid}')
print(f'Email = {account.email}')
print(f'Email verified = {account.email_verified}')
print(f'Droplet limit = {account.droplet_limit}')
print(f'Floating IP limit = {account.floating_ip_limit}')
print(f'Volume limit = {account.volume_limit}')
