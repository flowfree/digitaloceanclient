import json 

import pytest
import responses

from .models.test_action import action_model_matches
from .models.test_snapshot import snapshot_model_matches
from .models.test_volume import volume_model_matches


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
        assert volume_model_matches(volume, expected)


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
        assert volume_model_matches(volume, expected)

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
    assert volume_model_matches(volume, json_response['volume'])


@responses.activate
def test_retrieve_existing_volume(client, load_json):
    json_response = load_json('volume_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/volumes/506f78a4-e098-11e5-ad9f-000f53306ae1',
        json=json_response,
    )

    volume = client.volumes.get('506f78a4-e098-11e5-ad9f-000f53306ae1')
    assert volume_model_matches(volume, json_response['volume'])


@responses.activate
def test_create_snapshot_from_volume(client, load_json):
    json_response = load_json('snapshot_201_created.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/volumes/82a48a18-873f-11e6-96bf-000f53315a41/snapshots',
        json=json_response,
        status=201,
    )

    snapshot = client.volumes.create_snapshot(volume_id='82a48a18-873f-11e6-96bf-000f53315a41',
                                              name='big-data-snapshot1475261774')

    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/volumes/82a48a18-873f-11e6-96bf-000f53315a41/snapshots'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'name': 'big-data-snapshot1475261774',
    })
    assert snapshot_model_matches(snapshot, json_response['snapshot'])


@responses.activate
def test_delete_volume(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/volumes/1234567',
        status=204,
    )

    response = client.volumes.delete('1234567')

    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/volumes/1234567'
    assert response == None


@responses.activate
def test_attach_volume_to_droplet(client, load_json):
    json_response = load_json('action_attach_volume.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/volumes/7724db7c-e098-11e5-b522-000f53304e51/actions',
        json=json_response,
    )

    action = client.volumes.attach_to_droplet(volume_id='7724db7c-e098-11e5-b522-000f53304e51',
                                              droplet_id='11612190',
                                              region_slug='nyc1',
                                              tags=['aninterestingtag'])

    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
            'https://api.digitalocean.com/v2/volumes/7724db7c-e098-11e5-b522-000f53304e51/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'attach',
        'droplet_id': '11612190',
        'region': 'nyc1',
        'tags': ['aninterestingtag']
    })
    assert action_model_matches(action, json_response['action'])


def test_update_is_not_implemented(client):
    with pytest.raises(NotImplementedError) as e:
        client.volumes.update('1234567')
