import responses


@responses.activate
def test_get_all_keys(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account/keys',
        json=load_json('ssh_key_list.json')
    )

    keys = client.ssh_keys.all()

    key = next(keys)
    assert key.id == 512189
    assert key.fingerprint == '3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa'
    assert key.public_key == 'ssh-rsa AEXAMPLEaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example 1'
    assert key.name == 'My SSH Public Key #1'

    key = next(keys)
    assert key.id == 512190
    assert key.fingerprint == '3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fb'
    assert key.public_key == 'ssh-rsa AEXAMPLEaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example 2'
    assert key.name == 'My SSH Public Key #2'
