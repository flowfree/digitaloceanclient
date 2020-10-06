import json 

import pytest
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


class TestCreateNewCustomCertificate:
    def test_invalid_params(self, client):
        with pytest.raises(ValueError) as e:
            certificate = client.certificates.create(
                type_='custom',
                name='le-cert-01',
                dns_names=['www.example.com', 'example.com'],
            )

    @responses.activate
    def test_correct(self, client, load_json):
        json_response = load_json('certificate_single_custom.json')
        responses.add(
            responses.POST,
            'https://api.digitalocean.com/v2/certificates',
            json=json_response,
            status=201,
        )

        certificate = client.certificates.create(
            type_='custom',
            name='web-cert-01',
            private_key='<contents_of_private_key>',
            leaf_certificate='<contents_of_leaf_certificate>',
            certificate_chain='<contents_of_certificate_chain>'
        )

        assert certificate_model_matches(certificate, json_response['certificate'])
        assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
            'type': 'custom',
            'name': 'web-cert-01',
            'private_key': '<contents_of_private_key>',
            'leaf_certificate': '<contents_of_leaf_certificate>',
            'certificate_chain': '<contents_of_certificate_chain>'
        })


class TestCreateNewLetsEncryptCertificate:
    def test_invalid_params(self, client):
        with pytest.raises(ValueError) as e:
            certificate = client.certificates.create(
                type_='lets_encrypt',
                name='web-cert-01',
                private_key='<contents_of_private_key>',
                leaf_certificate='<contents_of_leaf_certificate>',
                certificate_chain='<contents_of_certificate_chain>'
            )

    @responses.activate
    def test_correct(self, client, load_json):
        json_response = load_json('certificate_single_lets_encrypt.json')
        responses.add(
            responses.POST,
            'https://api.digitalocean.com/v2/certificates',
            json=json_response,
            status=202
        )

        certificate = client.certificates.create(
            type_='lets_encrypt',
            name='le-cert-01',
            dns_names=['www.example.com', 'example.com'],
        )

        assert certificate_model_matches(certificate, json_response['certificate'])
        assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
            "type": "lets_encrypt",
            "name": "le-cert-01",
            "dns_names": ["www.example.com", "example.com"]
        })


@responses.activate
def test_retrieve_existing_certificate(client, load_json):
    json_response = load_json('certificate_single_custom.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/certificates/1234567',
        json=json_response,
    )

    cert = client.certificates.get('1234567')
    assert certificate_model_matches(cert, json_response['certificate'])


def test_update_is_not_supported(client):
    with pytest.raises(NotImplementedError) as e:
        client.certificates.update('aaa', 'bbb', 'ccc')


@responses.activate
def test_delete_certificate(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/certificates/1234567',
        status=204,
    )

    cert = client.certificates.delete('1234567')

    assert cert is None
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/certificates/1234567'
