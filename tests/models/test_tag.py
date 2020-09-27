from digitaloceanclient.models import Tag 


def test_load_from_json(load_json):
    json_response = load_json('single_tag.json')
    data = json_response['tag']

    tag = Tag(data)

    assert tag.name == data['name']
    assert tag.resources.count == data['resources']['count']
    assert tag.resources.last_tagged_uri == data['resources']['last_tagged_uri']
    assert tag.resources.droplets.count == data['resources']['droplets']['count']
    assert tag.resources.droplets.last_tagged_uri == data['resources']['droplets']['last_tagged_uri']
    assert tag.resources.images.count == data['resources']['images']['count']
    assert tag.resources.images.last_tagged_uri == data['resources']['images']['last_tagged_uri']
    assert tag.resources.volumes.count == data['resources']['volumes']['count']
    assert tag.resources.volumes.last_tagged_uri == data['resources']['volumes']['last_tagged_uri']
    assert tag.resources.volume_snapshots.count == data['resources']['volume_snapshots']['count']
    assert tag.resources.volume_snapshots.last_tagged_uri == data['resources']['volume_snapshots']['last_tagged_uri']
    assert tag.resources.databases.count == data['resources']['databases']['count']
    assert tag.resources.databases.last_tagged_uri == data['resources']['databases']['last_tagged_uri']
