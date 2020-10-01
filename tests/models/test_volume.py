from digitaloceanclient.models import Volume 


def test_load_from_json():
    data = {
        "id":"506f78a4-e098-11e5-ad9f-000f53306ae1",
        "region":{
            "name":"New York 1",
            "slug":"nyc1",
            "sizes":[
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
            "features":[
                "private_networking",
                "backups",
                "ipv6",
                "metadata"
            ],
            "available": True
        },
        "droplet_ids":[],
        "name":"example",
        "description":"Block store for examples",
        "size_gigabytes":10,
        "created_at":"2016-03-02T17:00:49Z",
        "filesystem_type":"ext4",
        "filesystem_label":"example",
        "tags":["aninterestingtag"]
    }

    volume = Volume(data)

    assert volume_model_matches(volume, data)
    assert volume.tags == ['aninterestingtag']


def volume_model_matches(volume, expected):
    """
    Helper function to check the Volume model against the expected dict.
    """
    return volume.id == expected['id'] and \
           volume.region.name == expected['region']['name'] and \
           volume.region.slug == expected['region']['slug'] and \
           volume.region.sizes == expected['region']['sizes'] and \
           volume.region.features == expected['region']['features'] and \
           volume.region.available == expected['region']['available'] and \
           volume.droplet_ids == expected['droplet_ids'] and \
           volume.name == expected['name'] and \
           volume.description == expected['description'] and \
           volume.size_gigabytes == expected['size_gigabytes'] and \
           volume.created_at == expected['created_at'] and \
           volume.filesystem_type == expected['filesystem_type'] and \
           volume.filesystem_label == expected['filesystem_label']
