import responses 


@responses.activate
def test_list_all_snapshots(client, load_json):
    json_response = load_json('snapshot_list.json')

    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/snapshots',
        json=json_response,
    )

    rows = client.snapshots.all()

    snapshot = next(rows)
    expected = json_response['snapshots'][0]
    assert snapshot.id == expected['id']
    assert snapshot.name == expected['name']
    assert snapshot.regions == expected['regions']
    assert snapshot.created_at == expected['created_at']
    assert snapshot.resource_id == expected['resource_id']
    assert snapshot.resource_type == expected['resource_type']
    assert snapshot.min_disk_size == expected['min_disk_size']
    assert snapshot.size_gigabytes == expected['size_gigabytes']
    assert snapshot.tags == expected['tags']

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/snapshots'
