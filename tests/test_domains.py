import json 

import pytest
import responses 


@responses.activate
def test_list_all_domains(client, load_json):
    json_response = load_json('domain_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/domains',
        json=json_response,
        status=200,
    )

    all_domains = client.domains.all()

    for expected in json_response['domains']:
        domain = next(all_domains)
        assert domain.name == expected['name']
        assert domain.ttl == expected['ttl']
        assert domain.zone_file == expected['zone_file']
    
    assert len(responses.calls) == 1


@responses.activate
def test_create_new_domain(client, load_json):
    json_response = load_json('domain_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/domains',
        json=json_response,
        status=201,
    )

    domain = client.domains.create(
        name='example.com',
        ip_address='1.2.3.4',
    )

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/domains'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'name': 'example.com',
        'ip_address': '1.2.3.4',
    })

    expected = json_response['domain']
    assert domain.name == expected['name']
    assert domain.ttl == expected['ttl']
    assert domain.zone_file == expected['zone_file']


@responses.activate
def test_retrieve_existing_domain(client, load_json):
    json_response = load_json('domain_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/domains/example.com',
        json=json_response,
        status=200,
    )

    domain = client.domains.get(name='example.com')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/domains/example.com'

    expected = json_response['domain']
    assert domain.name == expected['name']
    assert domain.ttl == expected['ttl']
    assert domain.zone_file == expected['zone_file']


def test_update_is_not_supported(client):
    with pytest.raises(NotImplementedError) as e:
        client.domains.update(name='updated.com')


@responses.activate
def test_delete_domain(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/domains/example.com',
        status=204,
    )

    response = client.domains.delete(name='example.com')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/domains/example.com'
    assert response is None
