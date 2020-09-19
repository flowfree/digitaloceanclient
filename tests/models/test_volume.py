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

    assert volume.id == '506f78a4-e098-11e5-ad9f-000f53306ae1'
    assert volume.region.name == 'New York 1'
    assert volume.region.slug == 'nyc1'
    assert volume.region.sizes == [
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
    ]
    assert volume.region.features == [
        "private_networking",
        "backups",
        "ipv6",
        "metadata"
    ]
    assert volume.region.available == True
    assert volume.droplet_ids == []
    assert volume.name == 'example'
    assert volume.description == 'Block store for examples'
    assert volume.size_gigabytes == 10
    assert volume.created_at == '2016-03-02T17:00:49Z'
    assert volume.filesystem_type == 'ext4'
    assert volume.filesystem_label == 'example'
    assert volume.tags == ['aninterestingtag']
