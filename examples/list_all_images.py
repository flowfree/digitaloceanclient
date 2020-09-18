import os
from digitaloceanclient import DigitalOceanClient

"""
List all images, you might want to cache the result.
"""

access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)

total = 0
for image in do.images.all():
    print(f'ID = {image.id}')
    print(f'Name = {image.name}')
    print(f'Description = {image.description}')
    print(f'Slug = {image.slug}')
    print(f'Distribution = {image.distribution}')
    print(f'Public = {image.public}')
    print(f'Regions = {image.regions}')
    print(f'Created at = {image.created_at}')
    print(f'Min disk size = {image.min_disk_size} GB')
    print(f'Type = {image.type}')
    print(f'Size = {image.size_gigabytes} GB')
    print(f'Tags = {image.tags}')
    print(f'Status = {image.status}')
    print(f'---')
    total += 1

print(f'Total = {total}')
