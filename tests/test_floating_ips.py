import json 

import pytest
import responses

from .models.test_floating_ip import floating_ip_model_matches


@responses.activate
def test_retrieve_all_floating_ips(client, load_json):
    json_response = load_json('floating_ip_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/floating_ips',
        json=json_response,
        status=200,
    )

    rows = client.floating_ips.all()

    for expected in json_response['floating_ips']:
        m = next(rows)
        assert floating_ip_model_matches(m, expected)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips'


@responses.activate
def test_create_new_floating_ip_assigned_to_a_droplet(client, load_json):
    json_response = load_json('floating_ip_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/floating_ips',
        json=json_response,
        status=202,
    )

    floating_ip = client.floating_ips.create(droplet_id='123456')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'droplet_id': '123456'
    })
    assert floating_ip_model_matches(floating_ip, json_response['floating_ip'])


@responses.activate
def test_create_new_floating_ip_reserved_to_a_region(client, load_json):
    json_response = load_json('floating_ip_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/floating_ips',
        json=json_response,
        status=202,
    )

    floating_ip = client.floating_ips.create(region_slug='nyc3')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'region': 'nyc3'
    })
    assert floating_ip_model_matches(floating_ip, json_response['floating_ip'])


@responses.activate
def test_retrieve_a_floating_ip(client, load_json):
    json_response = load_json('floating_ip_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/floating_ips/45.55.96.47',
        json=json_response,
        status=200,
    )

    floating_ip = client.floating_ips.get(floating_ip_addr='45.55.96.47')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/floating_ips/45.55.96.47'
    assert floating_ip_model_matches(floating_ip, json_response['floating_ip'])
