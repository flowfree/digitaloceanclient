from digitaloceanclient.models import Certificate


def test_populate_from_json():
    data = {
        "id": "892071a0-bb95-49bc-8021-3afd67a210bf",
        "name": "web-cert-01",
        "not_after": "2017-02-22T00:23:00Z",
        "sha1_fingerprint": "dfcc9f57d86bf58e321c2c6c31c7a971be244ac7",
        "created_at": "2017-02-08T16:02:37Z",
        "dns_names": ["example1.com", "example2.com"],
        "state": "verified",
        "type": "custom"
    }

    certificate = Certificate(data)
    assert certificate_model_matches(certificate, data)


def certificate_model_matches(cert, dict_):
    return cert.id == dict_['id'] and \
           cert.name == dict_['name'] and \
           cert.not_after == dict_['not_after'] and \
           cert.sha1_fingerprint == dict_['sha1_fingerprint'] and \
           cert.created_at == dict_['created_at'] and \
           cert.dns_names == dict_['dns_names'] and \
           cert.state == dict_['state'] and \
           cert.type == dict_['type']
