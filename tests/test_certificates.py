import responses

from .models.test_certificate import certificate_model_matches


@responses.activate
def test_list_all_certificates(client, load_json):
    json_response = load_json('certificate_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/certificates',
        json=json_response,
        status=200,
    )

    rows = client.certificates.all()

    for expected in json_response['certificates']:
        certificate = next(rows)
        assert certificate_model_matches(certificate, expected)
