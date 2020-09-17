import os
from digitaloceanclient import DigitalOceanClient

"""
List all regions, you might want to cache the result.
"""

access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)

for region in do.regions.all():
    print(f'Name = {region.name}')
    print(f'Slug = {region.slug}')
    print(f'Available = {region.available}')
    print(f'Features = {region.features}')
    print(f'Sizes = {region.sizes}')
    print(f'---')
