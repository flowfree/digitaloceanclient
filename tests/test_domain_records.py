import json 

import pytest
import responses

from .models.test_domain_record import domain_record_model_matches


@responses.activate
def test_retrieve_all_records(client, load_json):
    json_response = load_json('domain_record_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/domains/example.com/records',
        json=json_response,
        status=200,
    )

    records = client.domain_records.all(for_domain='example.com')

    for expected in json_response['domain_records']:
        record = next(records)
        assert domain_record_model_matches(record, expected)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/domains/example.com/records'


@responses.activate
def test_filter_domain_records(client, load_json):
    json_response = load_json('domain_record_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/domains/example.com/records',
        json=json_response,
        status=200,
    )

    records = client.domain_records.all(for_domain='example.com', 
                                        name='sub.example.com')
    next(records)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2' \
           '/domains/example.com/records?name=sub.example.com'

    records = client.domain_records.all(for_domain='example.com', 
                                        type_='MX')
    next(records)
    assert len(responses.calls) == 2
    assert responses.calls[1].request.method == 'GET'
    assert responses.calls[1].request.url == \
           'https://api.digitalocean.com/v2' \
           '/domains/example.com/records?type=MX'

    records = client.domain_records.all(for_domain='example.com', 
                                        name='sub.example.com',
                                        type_='MX')
    next(records)
    assert len(responses.calls) == 3
    assert responses.calls[2].request.method == 'GET'
    assert responses.calls[2].request.url == \
           'https://api.digitalocean.com/v2' \
           '/domains/example.com/records?name=sub.example.com&type=MX'


@responses.activate
def test_create_new_domain_record(client, load_json):
    json_response = load_json('domain_record_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/domains/example.com/records',
        json=json_response,
        status=201,
    )

    record = client.domain_records.create(
        for_domain='example.com',
        type_='A',
        name='www',
        data='162.10.66.0',
        ttl=1800,
    )

    assert domain_record_model_matches(record, json_response['domain_record'])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/domains/example.com/records'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'A',
        'name': 'www',
        'data': '162.10.66.0',
        'ttl': 1800,
    })


@responses.activate
def test_retrieve_existing_domain_record(client, load_json):
    json_response = load_json('domain_record_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/domains/example.com/records/3352896',
        json=json_response,
        status=200,
    )

    record = client.domain_records.get(for_domain='example.com', id_='3352896')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/domains/example.com/records/3352896'
    assert domain_record_model_matches(record, json_response['domain_record'])
