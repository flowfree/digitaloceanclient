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
    assert cdn_endpoint_model_matches(cdn, data)


def cdn_endpoint_model_matches(endpoint, expected):
    return endpoint.id == expected['id'] and \
           endpoint.origin == expected['origin'] and \
           endpoint.endpoint == expected['endpoint'] and \
           endpoint.created_at == expected['created_at'] and \
           endpoint.certificate_id == expected['certificate_id'] and \
           endpoint.custom_domain == expected['custom_domain'] and \
           endpoint.ttl == expected['ttl']
