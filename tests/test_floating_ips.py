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
