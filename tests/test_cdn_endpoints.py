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
