import json

import pytest
import responses

from .models.test_firewall import model_matches


@responses.activate
def test_list_all_firewalls(client, load_json):
    json_response = load_json('firewall_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/firewalls',
        json=json_response,
        status=200,
    )

    rows = client.firewalls.all()

    for expected in json_response['firewalls']:
        firewall = next(rows)
        assert model_matches(firewall, expected)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/firewalls'


@responses.activate
def test_create_new_firewall(client, load_json):
    json_response = load_json('firewall_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/firewalls',
        json=json_response,
        status=201,
    )

    inbound_rules = [{
        "protocol": "tcp",
        "ports": "80",
        "sources": {"load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"]}
    }, {
        "protocol": "tcp",
        "ports": "22",
        "sources": {
            "tags": ["gateway"],
            "addresses": ["18.0.0.0/8"]
        }
    }]
    outbound_rules = [{
        "protocol": "tcp",
        "ports": "80",
        "destinations": {
            "addresses": ["0.0.0.0/0", "::/0"]
        }
    }]
    firewall = client.firewalls.create(name='firewall',
                                       inbound_rules=inbound_rules,
                                       outbound_rules=outbound_rules,
                                       droplet_ids=[8043964])

    assert model_matches(firewall, json_response['firewall'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/firewalls'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        "name": "firewall",
        "inbound_rules": [{
            "protocol": "tcp",
            "ports": "80",
            "sources": {"load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"]}
        },{
            "protocol": "tcp",
            "ports": "22",
            "sources": {
                "tags": ["gateway"],
                "addresses": ["18.0.0.0/8"]
            }
        }],
        "outbound_rules": [{
            "protocol": "tcp",
            "ports": "80",
            "destinations": {
                "addresses": ["0.0.0.0/0", "::/0"]
            }
        }],
        "droplet_ids": [8043964]
    })


@responses.activate
def test_retrieve_existing_firewall(client, load_json):
    json_response = load_json('firewall_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c',
        json=json_response,
        status=200,
    )

    firewall = client.firewalls.get('bb4b2611-3d72-467b-8602-280330ecd65c')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c'
    assert model_matches(firewall, json_response['firewall'])


@responses.activate
def test_update_existing_firewall(client, load_json):
    json_response = load_json('firewall_single.json')
    responses.add(
        responses.PUT,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c',
        json=json_response,
        status=202,
    )

    inbound_rules = [{
        "protocol": "tcp",
        "ports": "80",
        "sources": {"load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"]}
    }, {
        "protocol": "tcp",
        "ports": "22",
        "sources": {
            "tags": ["gateway"],
            "addresses": ["18.0.0.0/8"]
        }
    }]
    outbound_rules = [{
        "protocol": "tcp",
        "ports": "80",
        "destinations": {
            "addresses": ["0.0.0.0/0", "::/0"]
        }
    }]
    firewall = client.firewalls.update(firewall_id='bb4b2611-3d72-467b-8602-280330ecd65c',
                                       name='firewall',
                                       inbound_rules=inbound_rules,
                                       outbound_rules=outbound_rules,
                                       droplet_ids=[8043964])

    assert model_matches(firewall, json_response['firewall'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'PUT'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        "name": "firewall",
        "inbound_rules": [{
            "protocol": "tcp",
            "ports": "80",
            "sources": {"load_balancer_uids": ["4de7ac8b-495b-4884-9a69-1050c6793cd6"]}
        },{
            "protocol": "tcp",
            "ports": "22",
            "sources": {
                "tags": ["gateway"],
                "addresses": ["18.0.0.0/8"]
            }
        }],
        "outbound_rules": [{
            "protocol": "tcp",
            "ports": "80",
            "destinations": {
                "addresses": ["0.0.0.0/0", "::/0"]
            }
        }],
        "droplet_ids": [8043964]
    })


@responses.activate
def test_delete_firewall(client, load_json):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c',
        status=204,
    )

    response = client.firewalls.delete('bb4b2611-3d72-467b-8602-280330ecd65c')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c'
    assert response is None


@responses.activate
def test_add_droplets_to_existing_firewall(client):
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/droplets',
        status=204,
    )

    response = client.firewalls.add_droplets(firewall_id='bb4b2611-3d72-467b-8602-280330ecd65c',
                                             droplet_ids=['49696269'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/droplets'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'droplet_ids': ['49696269']
    })
    assert response is None


@responses.activate
def test_remove_droplets_from_firewall(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/droplets',
        status=204,
    )

    response = client.firewalls.remove_droplets(firewall_id='bb4b2611-3d72-467b-8602-280330ecd65c',
                                                droplet_ids=['49696269'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/droplets'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'droplet_ids': ['49696269']
    })
    assert response is None


@responses.activate
def test_assign_tags_to_a_firewall(client):
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/tags',
        status=204,
    )

    response = client.firewalls.add_tags(firewall_id='bb4b2611-3d72-467b-8602-280330ecd65c',
                                         tags=['frontend'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/tags'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'tags': ['frontend']
    })
    assert response is None


@responses.activate
def test_remove_tags_from_firewall(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/tags',
        status=204,
    )

    response = client.firewalls.remove_tags(firewall_id='bb4b2611-3d72-467b-8602-280330ecd65c',
                                            tags=['frontend'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/firewalls/bb4b2611-3d72-467b-8602-280330ecd65c/tags'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'tags': ['frontend']
    })
    assert response is None
