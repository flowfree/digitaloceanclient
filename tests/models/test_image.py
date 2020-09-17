from digitaloceanclient.models import Image


def test_load_from_json():
    data = {
        "id": 7555620,
        "name": "Nifty New Snapshot",
        "distribution": "Ubuntu",
        "slug": None,
        "public": False,
        "regions": ["nyc2", "nyc3"],
        "created_at": "2014-11-04T22:23:02Z",
        "type": "snapshot",
        "min_disk_size": 20,
        "size_gigabytes": 2.34,
        "description": "",
        "tags": [],
        "status": "available",
        "error_message": ""
    }

    image = Image.from_json(data)

    assert image.id == 7555620
    assert image.name == 'Nifty New Snapshot'
    assert image.distribution == 'Ubuntu'
    assert image.slug == None
    assert image.public == False
    assert image.regions == ['nyc2', 'nyc3']
    assert image.created_at == '2014-11-04T22:23:02Z'
    assert image.type == Image.TYPE_SNAPSHOT
    assert image.min_disk_size == 20
    assert image.size_gigabytes == 2.34
    assert image.description == ''
    assert image.tags == []
    assert image.status == Image.STATUS_AVAILABLE
