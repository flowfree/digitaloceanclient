from digitaloceanclient.models import FloatingIPAction


def test_load_from_json():
    data = {
        "id": 68212728,
        "status": "in-progress",
        "type": "assign_ip",
        "started_at": "2015-10-15T17:45:44Z",
        "completed_at": None,
        "resource_id": 758603823,
        "resource_type": "floating_ip",
        "region": {
            "name": "New York 3",
            "slug": "nyc3",
            "sizes": [
                "s-1vcpu-1gb",
                "s-1vcpu-2gb",
                "s-1vcpu-3gb",
                "s-2vcpu-2gb",
                "s-3vcpu-1gb",
                "s-2vcpu-4gb",
                "s-4vcpu-8gb",
                "s-6vcpu-16gb",
                "s-8vcpu-32gb",
                "s-12vcpu-48gb",
                "s-16vcpu-64gb",
                "s-20vcpu-96gb",
                "s-24vcpu-128gb",
                "s-32vcpu-192gb"
            ],
            "features": [
                "private_networking",
                "backups",
                "ipv6",
                "metadata"
            ],
            "available": True
        },
        "region_slug": "nyc3"
    }

    action = FloatingIPAction(data)

    assert action.id == data['id']
    assert action.status == data['status']
    assert action.type == data['type']
    assert action.started_at == data['started_at']
    assert action.completed_at == data['completed_at']
    assert action.resource_id == data['resource_id']
    assert action.resource_type == data['resource_type']
    assert action.region.name == data['region']['name']
    assert action.region.slug == data['region']['slug']
    assert action.region.sizes == data['region']['sizes']
    assert action.region.features == data['region']['features']
    assert action.region.available == data['region']['available']
    assert action.region_slug == data['region_slug']
