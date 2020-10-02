import json 

import responses 

from .models.test_cdn_endpoint import cdn_endpoint_model_matches


@responses.activate
def test_list_all_cdn_endpoints(client, load_json):
    json_response = load_json('cdn_endpoint_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/cdn/endpoints',
        json=json_response
    )

    rows = client.cdn_endpoints.all()

    for expected in json_response['endpoints']:
        assert cdn_endpoint_model_matches(next(rows), expected)


@responses.activate
def test_create_new_cdn_endpoint(client, load_json):
    json_response = load_json('cdn_endpoint_201_created.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/cdn/endpoints',
        json=json_response,
    )

    endpoint = client.cdn_endpoints.create(
        origin='static-images.nyc3.digitaloceanspaces.com',
        certificate_id='892071a0-bb95-49bc-8021-3afd67a210bf',
        custom_domain='static.example.com',
        ttl=3600
    )

    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/cdn/endpoints'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'origin': 'static-images.nyc3.digitaloceanspaces.com',
        'certificate_id': '892071a0-bb95-49bc-8021-3afd67a210bf',
        'custom_domain': 'static.example.com',
        'ttl': 3600
    })
    assert cdn_endpoint_model_matches(endpoint, json_response['endpoint'])
