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
