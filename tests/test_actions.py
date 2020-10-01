import pytest
import responses

from digitaloceanclient.models import Action


@responses.activate
def test_list_all_actions(client, load_json):
    json_response = load_json('action_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/actions',
        json=json_response
    )

    rows = client.actions.all()

    for expected in json_response['actions']:
        action = next(rows)
        assert action.id == expected['id']
        assert action.status == expected['status']
        assert action.type == expected['type']
        assert action.started_at == expected['started_at']
        assert action.completed_at == expected['completed_at']
        assert action.resource_id == expected['resource_id']
        assert action.resource_type == expected['resource_type']
        assert action.region.name == expected['region']['name']
        assert action.region.slug == expected['region']['slug']
        assert action.region.sizes == expected['region']['sizes']
        assert action.region.features == expected['region']['features']
        assert action.region.available == expected['region']['available']
        assert action.region_slug == expected['region_slug']


@responses.activate
def test_refresh_action(client, load_json):
    json_response1 = load_json('action_create_droplet_in_progress.json')
    json_response2 = load_json('action_create_droplet_completed.json')

    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/actions/36804636',
        json=json_response1
    )
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/actions/36804636',
        json=json_response2
    )

    action = Action({'id': '36804636'})

    client.actions.refresh(action)
    assert action.id == json_response1['action']['id']
    assert action.type == json_response1['action']['type']
    assert action.resource_id == json_response1['action']['resource_id']
    assert action.resource_type == json_response1['action']['resource_type']
    assert action.is_in_progress()

    client.actions.refresh(action)
    assert action.id == json_response1['action']['id']
    assert action.type == json_response1['action']['type']
    assert action.resource_id == json_response1['action']['resource_id']
    assert action.resource_type == json_response1['action']['resource_type']
    assert action.is_completed()


@responses.activate
def test_retrieve_an_action(client, load_json):
    json_response = load_json('action_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/actions/36804636',
        json=json_response,
    )

    action = client.actions.get('36804636')

    expected = json_response['action']
    assert action.id == expected['id']
    assert action.status == expected['status']
    assert action.type == expected['type']
    assert action.started_at == expected['started_at']
    assert action.completed_at == expected['completed_at']
    assert action.resource_id == expected['resource_id']
    assert action.resource_type == expected['resource_type']
    assert action.region.name == expected['region']['name']
    assert action.region.slug == expected['region']['slug']
    assert action.region.sizes == expected['region']['sizes']
    assert action.region.features == expected['region']['features']
    assert action.region.available == expected['region']['available']
    assert action.region_slug == expected['region_slug']


@responses.activate
def test_refresh_get_malformed_response(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/actions/36804636',
        json={'aaa': 'bbb'}
    )

    action = Action({'id': '36804636'})

    with pytest.raises(client.MalformedResponse) as e:
        client.actions.refresh(action)


def test_create_is_unsupported(client):
    with pytest.raises(NotImplementedError) as e:
        client.actions.create('aaa', 'bbb', 'ccc')


def test_update_is_unsupported(client):
    with pytest.raises(NotImplementedError) as e:
        client.actions.update('12345')


def test_delete_is_unsupported(client):
    with pytest.raises(NotImplementedError) as e:
        client.actions.delete('12345')


def action_model_matches(action, expected):
    return action.id == expected['id'] and \
           action.status == expected['status'] and \
           action.type == expected['type'] and \
           action.started_at == expected['started_at'] and \
           action.completed_at == expected['completed_at'] and \
           action.resource_id == expected['resource_id'] and \
           action.resource_type == expected['resource_type'] and \
           action.region.name == expected['region']['name'] and \
           action.region.slug == expected['region']['slug'] and \
           action.region.sizes == expected['region']['sizes'] and \
           action.region.features == expected['region']['features'] and \
           action.region.available == expected['region']['available'] and \
           action.region_slug == expected['region_slug']
