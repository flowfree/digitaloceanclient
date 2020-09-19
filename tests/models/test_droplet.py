from digitaloceanclient.models import Droplet 


def test_populate_model_from_json(load_json):
    data = load_json('single_droplet.json')

    droplet = Droplet(data['droplet'])

    assert droplet.id == 1111111
    assert droplet.name == 'ubuntu-18-server'
    assert droplet.memory == 1024
    assert droplet.vcpus == 1
    assert droplet.disk == 25
    assert droplet.locked == False
    assert droplet.status == Droplet.STATUS_ACTIVE
    assert droplet.created_at == '2014-11-14T16:36:31Z'
    assert droplet.features == ['ipv6', 'virtio']
    assert droplet.backup_ids == []
    assert droplet.snapshot_ids == [7938206]
    assert droplet.volume_ids == []
    assert droplet.size == {}
    assert droplet.size_slug == 's-1vcpu-1gb'
    assert droplet.tags == []
    assert droplet.vpc_uuid == 'f9b0769c-e118-42fb-a0c4-fed15ef69662'

    assert droplet.kernel.id == 2233
    assert droplet.kernel.name == 'Ubuntu 14.04 x64 vmlinuz-3.13.0-37-generic'
    assert droplet.kernel.version == '3.13.0-37-generic'

    assert droplet.image.id == 6918990
    assert droplet.image.name == '14.04 x64'
    assert droplet.image.distribution == 'Ubuntu'
    assert droplet.image.slug == 'ubuntu-16-04-x64'
    assert droplet.image.public == True
    assert droplet.image.regions == [
        'nyc1', 
        'ams1', 
        'sfo1', 
        'nyc2', 
        'ams2', 
        'sgp1', 
        'lon1', 
        'nyc3', 
        'ams3', 
        'nyc3',
    ]
    assert droplet.image.created_at == '2014-10-17T20:24:33Z'
    assert droplet.image.type == 'snapshot'
    assert droplet.image.min_disk_size == 20
    assert droplet.image.size_gigabytes == 2.34

    assert droplet.region.slug == 'nyc3'
    assert droplet.region.name == 'New York 3'
    assert droplet.region.sizes == [
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
    assert droplet.region.available == True
    assert droplet.region.features == [
        "virtio",
        "private_networking",
        "backups",
        "ipv6",
        "metadata"
    ]
