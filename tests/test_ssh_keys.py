import responses


@responses.activate
def test_get_all_keys(client, load_json):
    json_response = load_json('ssh_key_list.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account/keys',
        json=json_response
    )

    keys = client.ssh_keys.all()

    key = next(keys)
    assert key.id == json_response['ssh_keys'][0]['id']
    assert key.fingerprint == json_response['ssh_keys'][0]['fingerprint']
    assert key.public_key == json_response['ssh_keys'][0]['public_key']
    assert key.name == json_response['ssh_keys'][0]['name']

    key = next(keys)
    assert key.id == json_response['ssh_keys'][1]['id']
    assert key.fingerprint == json_response['ssh_keys'][1]['fingerprint']
    assert key.public_key == json_response['ssh_keys'][1]['public_key']
    assert key.name == json_response['ssh_keys'][1]['name']
