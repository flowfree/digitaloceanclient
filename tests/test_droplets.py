import responses
    

@responses.activate
def test_list_all_droplets(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/droplets',
        json=load_json('droplet_list.json')
    )

    droplets = client.droplets.all()

    droplet = next(droplets)
    assert droplet.id == 3164444 
    assert droplet.name == 'example.com'
    assert droplet.created_at == '2014-11-14T16:29:21Z'

    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/droplets'
    assert responses.calls[0].request.headers['Authorization'] == 'Bearer TEST_TOKEN'


@responses.activate
def test_get_droplet(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/droplets/1111111',
        json=load_json('single_droplet.json')
    )

    droplet = client.droplets.get('1111111')

    assert droplet.id == 1111111
    assert droplet.name == 'ubuntu-18-server'
    assert droplet.memory == 1024
    assert droplet.vcpus == 1
