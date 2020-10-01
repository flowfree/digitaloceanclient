import json 

import responses


@responses.activate
def test_list_all_volumes(client, load_json):
    json_response = load_json('volume_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/volumes', 
        json=json_response
    )

    rows = client.volumes.all()

    for expected in json_response['volumes']:
        volume = next(rows)
        assert model_matches(volume, expected)


@responses.activate
def test_list_all_volumes_filtered_by_name(client, load_json):
    json_response = load_json('volume_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/volumes',
        json=json_response
    )

    rows = client.volumes.all(name='example')

    for expected in json_response['volumes']:
        volume = next(rows)
        assert model_matches(volume, expected)

    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/volumes?name=example'


@responses.activate
def test_create_new_block_storage_volume(client, load_json):
    json_response = load_json('volume_201_created.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/volumes',
        json=json_response,
        status=201,
    )

    volume = client.volumes.create(name='example',
                                   region='nyc1',
                                   size_gigabytes=10,
                                   description='Block storage for examples',
                                   filesystem_type='ext4',
                                   filesystem_label='example')

    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/volumes'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'name': 'example',
        'region': 'nyc1',
        'size_gigabytes': 10,
        'description': 'Block storage for examples',
        'filesystem_type': 'ext4',
        'filesystem_label': 'example',
    })
    assert model_matches(volume, json_response['volume'])


@responses.activate
def test_retrieve_existing_volume(client, load_json):
    json_response = load_json('volume_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/volumes/506f78a4-e098-11e5-ad9f-000f53306ae1',
        json=json_response,
    )

    volume = client.volumes.get('506f78a4-e098-11e5-ad9f-000f53306ae1')
    assert model_matches(volume, json_response['volume'])


def model_matches(volume, expected):
    """
    Helper function to check the volume's attributes to match with the expected dict.
    """
    return volume.id == expected['id'] and \
           volume.region.name == expected['region']['name'] and \
           volume.region.slug == expected['region']['slug'] and \
           volume.region.sizes == expected['region']['sizes'] and \
           volume.region.features == expected['region']['features'] and \
           volume.region.available == expected['region']['available'] and \
           volume.droplet_ids == expected['droplet_ids'] and \
           volume.name == expected['name'] and \
           volume.description == expected['description'] and \
           volume.size_gigabytes == expected['size_gigabytes'] and \
           volume.created_at == expected['created_at'] and \
           volume.filesystem_type == expected['filesystem_type'] and \
           volume.filesystem_label == expected['filesystem_label']
