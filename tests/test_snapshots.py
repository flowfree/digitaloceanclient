import pytest
import responses 


@responses.activate
def test_list_all_snapshots(client, load_json):
    json_response = load_json('snapshot_list.json')

    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/snapshots',
        json=json_response,
    )

    rows = client.snapshots.all()

    snapshot = next(rows)
    expected = json_response['snapshots'][0]
    assert snapshot.id == expected['id']
    assert snapshot.name == expected['name']
    assert snapshot.regions == expected['regions']
    assert snapshot.created_at == expected['created_at']
    assert snapshot.resource_id == expected['resource_id']
    assert snapshot.resource_type == expected['resource_type']
    assert snapshot.min_disk_size == expected['min_disk_size']
    assert snapshot.size_gigabytes == expected['size_gigabytes']
    assert snapshot.tags == expected['tags']

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/snapshots'


@responses.activate
def test_list_all_droplet_snapshots(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/snapshots?resource_type=droplet',
        json=load_json('snapshot_list.json'),
        status=200,
    )

    rows = client.snapshots.all(resource_type='droplet')
    next(rows)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/snapshots?resource_type=droplet'


@responses.activate
def test_list_all_volume_snapshots(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/snapshots?resource_type=volume',
        json=load_json('snapshot_list.json'),
        status=200,
    )

    rows = client.snapshots.all(resource_type='volume')
    next(rows)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/snapshots?resource_type=volume'


def test_invalid_filter(client, load_json):
    with pytest.raises(ValueError) as e:
        client.snapshots.all(resource_type='abcdef')
    assert str(e.value) == 'Invalid resource type: abcdef'


@responses.activate
def test_retrieve_a_snapshot(client, load_json):
    json_response = load_json('single_snapshot.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/snapshots/fbe805e8-866b-11e6-96bf-000f53315a41',
        json=json_response,
        status=200,
    )

    snapshot = client.snapshots.get('fbe805e8-866b-11e6-96bf-000f53315a41')

    expected = json_response['snapshot']
    assert snapshot.id == expected['id']
    assert snapshot.name == expected['name']
    assert snapshot.regions == expected['regions']
    assert snapshot.created_at == expected['created_at']
    assert snapshot.resource_id == expected['resource_id']
    assert snapshot.resource_type == expected['resource_type']
    assert snapshot.min_disk_size == expected['min_disk_size']
    assert snapshot.size_gigabytes == expected['size_gigabytes']
    assert snapshot.tags == expected['tags']


@responses.activate
def test_delete_a_snapshot(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/snapshots/fbe805e8-866b-11e6-96bf-000f53315a41',
        status=204,
    )

    response = client.snapshots.delete('fbe805e8-866b-11e6-96bf-000f53315a41')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/snapshots/fbe805e8-866b-11e6-96bf-000f53315a41'
    assert response == None


def test_no_create(client):
    with pytest.raises(NotImplementedError) as e:
        client.snapshots.create('aaa', 'bbb', 'ccc')
