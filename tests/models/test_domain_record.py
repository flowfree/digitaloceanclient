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
    assert domain_record_model_matches(record, data)


def domain_record_model_matches(record, data):
    return record.id == data['id'] and \
           record.type == data['type'] and \
           record.name == data['name'] and \
           record.data == data['data'] and \
           record.priority == data['priority'] and \
           record.port == data['port'] and \
           record.ttl == data['ttl'] and \
           record.weight == data['weight'] and \
           record.flags == data['flags'] and \
           record.tag == data['tag']
