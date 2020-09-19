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

    assert certificate.id == '892071a0-bb95-49bc-8021-3afd67a210bf'
    assert certificate.name == 'web-cert-01'
    assert certificate.not_after == '2017-02-22T00:23:00Z'
    assert certificate.sha1_fingerprint == 'dfcc9f57d86bf58e321c2c6c31c7a971be244ac7'
    assert certificate.created_at == '2017-02-08T16:02:37Z'
    assert certificate.dns_names == ["example1.com", "example2.com"]
    assert certificate.state == Certificate.STATE_VERIFIED
    assert certificate.type == Certificate.TYPE_CUSTOM
