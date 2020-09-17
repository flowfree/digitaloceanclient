import os
from digitaloceanclient import DigitalOceanClient

"""
Get information about an individual Droplet given its ID.
"""

access_token = os.getenv('ACCESS_TOKEN')
droplet_id = os.getenv('DROPLET_ID', '12345')

do = DigitalOceanClient(access_token)

droplet = do.droplets.get(droplet_id)
print(f'ID = {droplet.id}')
print(f'Name = {droplet.name}')
print(f'Memory = {droplet.memory} MB')
print(f'Number of VCPUs = {droplet.vcpus}')
print(f'Disk size = {droplet.size} GB')
print(f'Locked = {droplet.locked}')
print(f'Status = {droplet.status}')
print(f'Created at = {droplet.created_at}')
print(f'Features = {droplet.features}')
print(f'Backup IDs = {droplet.backup_ids}')
print(f'Snapshot IDs = {droplet.snapshot_ids}')
print(f'Volume IDs = {droplet.volume_ids}')
print(f'Size slug = {droplet.size_slug}')
print(f'Tags = {droplet.tags}')
print(f'VPC UUID = {droplet.vpc_uuid}')
if droplet.kernel:
    print(f'Kernel ID = {droplet.kernel.id}')
    print(f'Kernel name = {droplet.kernel.name}')
    print(f'Kernel version = {droplet.kernel.version}')
if droplet.image:
    print(f'Image ID = {droplet.image.id}')
    print(f'Image name = {droplet.image.name}')
    print(f'Image distribution = {droplet.image.distribution}')
    print(f'Image slug = {droplet.image.slug}')
    print(f'Image type = {droplet.image.type}')
if droplet.region:
    print(f'Region slug = {droplet.region.slug}')
    print(f'Region name = {droplet.region.name}')
    print(f'Region features = {droplet.region.features}')
