from digitaloceanclient.models import DomainRecord


def test_load_from_json():
    data = {
        "id": 28448429,
        "type": "NS",
        "name": "@",
        "data": "ns1.digitalocean.com",
        "priority": None,
        "port": None,
        "ttl": 1800,
        "weight": None,
        "flags": None,
        "tag": None
    }

    record = DomainRecord(data)

    assert record.id == data['id']
    assert record.type == data['type']
    assert record.name == data['name']
    assert record.data == data['data']
    assert record.priority == data['priority']
    assert record.port == data['port']
    assert record.ttl == data['ttl']
    assert record.weight == data['weight']
    assert record.flags == data['flags']
    assert record.tag == data['tag']
