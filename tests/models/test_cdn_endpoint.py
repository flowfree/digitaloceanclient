from digitaloceanclient.models import CDNEndpoint


def test_load_from_json():
    data = {
        "id": "19f06b6a-3ace-4315-b086-499a0e521b76",
        "origin": "static-images.nyc3.digitaloceanspaces.com",
        "endpoint": "static-images.nyc3.cdn.digitaloceanspaces.com",
        "created_at": "2018-07-19T15:04:16Z",
        "certificate_id": "892071a0-bb95-49bc-8021-3afd67a210bf",
        "custom_domain": "static.example.com",
        "ttl": 3600
    }

    cdn = CDNEndpoint(data)

    assert cdn.id == '19f06b6a-3ace-4315-b086-499a0e521b76'
    assert cdn.origin == 'static-images.nyc3.digitaloceanspaces.com'
    assert cdn.endpoint == 'static-images.nyc3.cdn.digitaloceanspaces.com'
    assert cdn.created_at == '2018-07-19T15:04:16Z'
    assert cdn.certificate_id == '892071a0-bb95-49bc-8021-3afd67a210bf'
    assert cdn.custom_domain == 'static.example.com'
    assert cdn.ttl == 3600
