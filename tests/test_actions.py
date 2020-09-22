import pytest
import responses

from digitaloceanclient.models import Action


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
def test_refresh_get_malformed_response(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/actions/36804636',
        json={'aaa': 'bbb'}
    )

    action = Action({'id': '36804636'})

    with pytest.raises(client.MalformedResponse) as e:
        client.actions.refresh(action)
