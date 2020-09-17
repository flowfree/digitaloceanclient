import responses 


@responses.activate
def test_list_all_regions(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/regions',
        json=load_json('region_list.json')
    )

    regions = client.regions.all()

    data = load_json('region_list.json')
    expected_regions = data['regions']

    for idx, region in enumerate(regions):
        expected = expected_regions[idx]

        assert region.name == expected['name']
        assert region.slug == expected['slug']
        assert region.available == expected['available']
        assert region.features ==  expected['features']
        assert region.sizes == expected['sizes']
