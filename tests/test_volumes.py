import responses


@responses.activate
def test_list_all_volumes(client, load_json):
    json_response = load_json('volume_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/volumes', 
        json=json_response
    )

    rows = client.volumes.all()

    for expected in json_response['volumes']:
        volume = next(rows)
        assert volume.id == expected['id']
        assert volume.region.name == expected['region']['name']
        assert volume.region.slug == expected['region']['slug']
        assert volume.region.sizes == expected['region']['sizes']
        assert volume.region.features == expected['region']['features']
        assert volume.region.available == expected['region']['available']
        assert volume.droplet_ids == expected['droplet_ids']
        assert volume.name == expected['name']
        assert volume.description == expected['description']
        assert volume.size_gigabytes == expected['size_gigabytes']
        assert volume.created_at == expected['created_at']
        assert volume.filesystem_type == expected['filesystem_type']
        assert volume.filesystem_label == expected['filesystem_label']
        assert volume.tags == expected['tags']


@responses.activate
def test_list_all_volumes_filtered_by_name(client, load_json):
    json_response = load_json('volume_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/volumes',
        json=json_response
    )

    rows = client.volumes.all(name='example')

    next(rows)
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/volumes?name=example'
