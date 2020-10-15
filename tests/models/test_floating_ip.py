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


def floating_ip_model_matches(a, b):
    return a.ip == b['ip'] and \
           a.droplet == b['droplet'] and \
           a.region.name == b['region']['name'] and \
           a.region.slug == b['region']['slug'] and \
           a.region.sizes == b['region']['sizes'] and \
           a.region.features == b['region']['features'] and \
           a.region.available == b['region']['available']
