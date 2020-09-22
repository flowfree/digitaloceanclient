import json
import responses

from digitaloceanclient.models import SSHKey


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


@responses.activate
def test_get_single_key(client, load_json):
    json_response = load_json('single_ssh_key.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account/keys/512190',
        json=json_response
    )

    key = client.ssh_keys.get('512190')

    assert key.id == json_response['ssh_key']['id']
    assert key.fingerprint == json_response['ssh_key']['fingerprint']
    assert key.public_key == json_response['ssh_key']['public_key']
    assert key.name == json_response['ssh_key']['name']


@responses.activate
def test_add_new_ssh_key(client, load_json):
    json_response = load_json('single_ssh_key.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/account/keys',
        json=json_response,
        status=201
    )

    name = json_response['ssh_key']['name']
    public_key = json_response['ssh_key']['public_key']
    key = client.ssh_keys.create(name=name, public_key=public_key)

    assert type(key) == SSHKey
    assert key.id == json_response['ssh_key']['id']
    assert key.fingerprint == json_response['ssh_key']['fingerprint']
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/account/keys'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({'name': name,
                                                                          'public_key': public_key})


@responses.activate
def test_update_ssh_key(client, load_json):
    json_response = load_json('single_ssh_key.json')
    key_id = json_response['ssh_key']['id']
    key_name = json_response['ssh_key']['name']

    responses.add(
        responses.PUT,
        f'https://api.digitalocean.com/v2/account/keys/{key_id}',
        json=json_response,
        status=200
    )

    key = client.ssh_keys.update(key_id_or_fingerprint=key_id, name=key_name)

    assert type(key) == SSHKey
    assert key.id == json_response['ssh_key']['id']
    assert key.fingerprint == json_response['ssh_key']['fingerprint']
    assert responses.calls[0].request.method == 'PUT'
    assert responses.calls[0].request.url == f'https://api.digitalocean.com/v2/account/keys/{key_id}'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({'name': key_name})


@responses.activate
def test_delete_ssh_key(client):
    key_id = '1234567'
    responses.add(
        responses.DELETE,
        f'https://api.digitalocean.com/v2/account/keys/{key_id}',
        status=204
    )

    response = client.ssh_keys.delete(key_id_or_fingerprint=key_id)

    assert response == None
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == f'https://api.digitalocean.com/v2/account/keys/{key_id}'
    assert responses.calls[0].request.body == None
