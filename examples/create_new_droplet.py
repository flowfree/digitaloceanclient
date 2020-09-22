import json
import time
import os

from digitaloceanclient import DigitalOceanClient
from digitaloceanclient.models import Image


def get_user_input(message, items):
    print(f'\n{message}')
    for num, item in enumerate(items):
        print(f'{num+1}. {item}')
    selected_item = None
    while True:
        try:
            num = int(input(f'[1-{len(items)}]? '))
            if num not in range(1, len(items)+1):
                raise ValueError
            selected_item = items[num-1]
            break 
        except ValueError:
            pass
    print(f'Selected {selected_item.slug}')
    return selected_item


access_token = os.getenv('ACCESS_TOKEN')
do = DigitalOceanClient(access_token)

# Get the name of the droplet
droplet_name = input('Droplet name: ')

# Select image
images = [i for i in do.images.all(type_='distribution')]
images = sorted(images, key=lambda i: i.distribution)
selected_image = get_user_input('Choose distribution image:', images)

# Select size
sizes, prices =[], []
for size in do.sizes.all():
    price = size.price_monthly
    if price <= 60.0 and price not in prices: 
        prices.append(price)
        sizes.append(size)
selected_size = get_user_input('Choose size:', sizes)

# Select region
regions = [r for r 
           in do.regions.all() 
           if r.slug in selected_size.regions 
              and r.available == True]
selected_region = get_user_input('Choose region:', regions)

try:
    print('\nCreating droplet...', end='')
    droplet, action = do.droplets.create(droplet_name, 
                                         selected_image.slug, 
                                         selected_size.slug, 
                                         selected_region.slug)
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
    print(f'\nHTTP {e.status_code} - {e}')
