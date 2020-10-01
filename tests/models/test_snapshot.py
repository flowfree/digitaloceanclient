from digitaloceanclient.models import Snapshot


def test_load_from_json():
    data = {
        "id": 6372321,
        "name": "5.10 x64",
        "regions": [
            "nyc1",
            "ams1",
            "sfo1",
            "nyc2",
            "ams2",
            "sgp1",
            "lon1",
            "nyc3",
            "ams3",
            "fra1",
            "tor1"
        ],
        "created_at": "2014-09-26T16:40:18Z",
        "resource_id": 2713828,
        "resource_type": "droplet",
        "min_disk_size": 20,
        "size_gigabytes": 1.42,
        "tags": []
    }

    snapshot = Snapshot(data)

    assert snapshot.id == data['id']
    assert snapshot.name == data['name']
    assert snapshot.regions == data['regions']
    assert snapshot.created_at == data['created_at']
    assert snapshot.resource_id == data['resource_id']
    assert snapshot.resource_type == data['resource_type']
    assert snapshot.min_disk_size == data['min_disk_size']
    assert snapshot.size_gigabytes == data['size_gigabytes']
    assert snapshot.tags == data['tags']


def snapshot_model_matches(snapshot, expected):
    """
    Helper function to check the Snapshot model against the expected dict.
    """
    return snapshot.id == expected['id'] and \
           snapshot.name == expected['name'] and \
           snapshot.regions == expected['regions'] and \
           snapshot.created_at == expected['created_at'] and \
           snapshot.resource_id == expected['resource_id'] and \
           snapshot.resource_type == expected['resource_type'] and \
           snapshot.min_disk_size == expected['min_disk_size'] and \
           snapshot.size_gigabytes == expected['size_gigabytes'] and \
           snapshot.tags == expected['tags'] 
