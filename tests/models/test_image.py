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

    image = Image(data)
    assert model_matches(image, data)


def model_matches(a, b):
    is_match = True
    for key, val in b.items():
        print(f'image.{key} = {getattr(a, key)}')
        is_match &= val == getattr(a, key)
    return is_match
