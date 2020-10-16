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
    assert model_matches(action, data)


def model_matches(a, b):
    return a.id == b['id'] and \
           a.status == b['status'] and \
           a.type == b['type'] and \
           a.started_at == b['started_at'] and \
           a.completed_at == b['completed_at'] and \
           a.resource_id == b['resource_id'] and \
           a.resource_type == b['resource_type'] and \
           a.region.name == b['region']['name'] and \
           a.region.slug == b['region']['slug'] and \
           a.region.sizes == b['region']['sizes'] and \
           a.region.features == b['region']['features'] and \
           a.region.available == b['region']['available'] and \
           a.region_slug == b['region_slug'] 
