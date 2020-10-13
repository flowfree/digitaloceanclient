import responses 


@responses.activate
def test_list_all_domains(client, load_json):
    json_response = load_json('domain_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/domains',
        json=json_response,
        status=200,
    )

    all_domains = client.domains.all()

    for expected in json_response['domains']:
        domain = next(all_domains)
        assert domain.name == expected['name']
        assert domain.ttl == expected['ttl']
        assert domain.zone_file == expected['zone_file']
    
    assert len(responses.calls) == 1
