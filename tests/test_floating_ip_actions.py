import json 

import pytest
import responses

from .models.test_floating_ip_action import model_matches


@responses.activate
def test_list_all_floating_ip_actions(client, load_json):
    json_response = load_json('floating_ip_action_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions',
        json=json_response,
        status=200
    ) 
    
    data = client.floating_ip_actions.all(for_ip_addr='45.55.96.47')

    for expected in json_response['actions']:
        model = next(data)
        assert model_matches(model, expected)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions'


@responses.activate
def test_assign(client, load_json):
    json_response = load_json('floating_ip_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions',
        json=json_response,
        status=201
    ) 

    action = client.floating_ip_actions.assign(for_ip_addr='45.55.96.47',
                                               droplet_id='8219222')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'assign',
        'droplet_id': '8219222',
    })
    assert model_matches(action, json_response['action'])


@responses.activate
def test_unassign(client, load_json):
    json_response = load_json('floating_ip_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions',
        json=json_response,
        status=201
    ) 

    action = client.floating_ip_actions.unassign(for_ip_addr='45.55.96.47')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'unassign',
    })
    assert model_matches(action, json_response['action'])


@responses.activate
def test_retrieve_floating_ip_action(client, load_json):
    json_response = load_json('floating_ip_action_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions/72531856',
        json=json_response,
        status=200
    ) 

    action = client.floating_ip_actions.get(for_ip_addr='45.55.96.47',
                                            action_id='72531856')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips/45.55.96.47/actions/72531856'
    assert model_matches(action, json_response['action'])


def test_unsupported_methods(client):
    for method in ['create', 'update', 'delete']:
        with pytest.raises(NotImplementedError):
            f = getattr(client.floating_ip_actions, method)
            f()
