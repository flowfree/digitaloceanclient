from digitaloceanclient.models import FloatingIP


def test_load_from_json():
    data = {
        "ip": "45.55.96.47",
        "droplet": None,
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
        }
    }

    floating_ip = FloatingIP(data)

    assert floating_ip.ip == data['ip']
    assert floating_ip.droplet == data['droplet']
    assert floating_ip.region.name == data['region']['name']
    assert floating_ip.region.slug == data['region']['slug']
    assert floating_ip.region.sizes == data['region']['sizes']
    assert floating_ip.region.features == data['region']['features']
    assert floating_ip.region.available == data['region']['available']
