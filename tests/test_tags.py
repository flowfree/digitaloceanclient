import responses 


@responses.activate
def test_get_all_tags(client, load_json):
    json_response = load_json('tag_list.json')

    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/tags',
        json=json_response
    )

    rows = client.tags.all()

    row = next(rows)
    expected = json_response['tags'][0]
    assert row.name == expected['name']
    assert row.resources.count == expected['resources']['count']
    assert row.resources.last_tagged_uri == expected['resources']['last_tagged_uri']
    assert row.resources.droplets.count == expected['resources']['droplets']['count']
    assert row.resources.droplets.last_tagged_uri == expected['resources']['droplets']['last_tagged_uri']
