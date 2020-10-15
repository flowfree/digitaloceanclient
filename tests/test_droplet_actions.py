import json 

import pytest
import responses

from .models.test_droplet_action import droplet_action_model_matches


@responses.activate
def test_retrieve_an_action(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/droplets/3164444/actions/36804807',
        json=json_response,
        status=200
    )

    action = client.droplet_actions.get(droplet_id='3164444', 
                                        action_id='36804807')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/droplets/3164444/actions/36804807'
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_perform_actions(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    tests = (
        'enable_backups',
        'disable_backups',
        'reboot',
        'power_cycle',
        'shutdown',
        'power_off',
        'power_on',
        'password_reset',
        'enable_ipv6',
    )
    for task in tests:
        f = getattr(client.droplet_actions, task)
        action = f(droplet_id='3164444')
        assert responses.calls[-1].request.method == 'POST'
        assert responses.calls[-1].request.url == \
            'https://api.digitalocean.com/v2/droplets/3164444/actions'
        assert responses.calls[-1].request.body.decode('utf-8') == json.dumps({
            'type': task,
        })
        assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_restore(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    action = client.droplet_actions.restore(droplet_id='3164444',
                                            image_slug='ubuntu-18.04')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/droplets/3164444/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'restore',
        'image': 'ubuntu-18.04',
    })
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_resize(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    action = client.droplet_actions.resize(droplet_id='3164444',
                                           size_slug='1gb',
                                           disk=True)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/droplets/3164444/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'resize',
        'size': '1gb',
        'disk': True,
    })
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_rebuild(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    action = client.droplet_actions.rebuild(droplet_id='3164444',
                                            image_slug='ubuntu-18-04')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/droplets/3164444/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'rebuild',
        'image': 'ubuntu-18-04',
    })
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_rename(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    action = client.droplet_actions.rename(droplet_id='3164444',
                                           name='new-droplet-name')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/droplets/3164444/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'rename',
        'name': 'new-droplet-name',
    })
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_change_kernel(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    action = client.droplet_actions.change_kernel(droplet_id='3164444',
                                                  kernel=12345)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/droplets/3164444/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'change_kernel',
        'kernel': 12345,
    })
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_snapshot(client, load_json):
    json_response = load_json('droplet_action_single.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/3164444/actions',
        json=json_response,
        status=201
    )

    action = client.droplet_actions.snapshot(droplet_id='3164444',
                                             name='Latest Snapshot')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == \
        'https://api.digitalocean.com/v2/droplets/3164444/actions'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'type': 'snapshot',
        'name': 'Latest Snapshot',
    })
    assert droplet_action_model_matches(action, json_response['action'])


@responses.activate
def test_perform_actions_on_tagged_droplets(client, load_json):
    json_response = load_json('droplet_action_list.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets/actions',
        json=json_response,
        status=201
    )
    tests = (
        'enable_backups',
        'disable_backups',
        'power_cycle',
        'shutdown',
        'power_off',
        'power_on',
        'snapshot',
        'enable_ipv6',
    )
    for task in tests:
        f = getattr(client.droplet_actions, f'{task}_for_tag')
        actions = f(tag_name='prod-server')

        assert responses.calls[-1].request.method == 'POST'
        assert responses.calls[-1].request.url == \
            'https://api.digitalocean.com/v2/droplets/actions?tag_name=prod-server'
        assert responses.calls[-1].request.body.decode('utf-8') == json.dumps({
            'type': task,
        })
        for i, expected in enumerate(json_response['actions']):
            assert droplet_action_model_matches(actions[i], expected)


def test_unsupported_methods(client):
    methods = (
        'all',
        'create',
        'update',
        'delete',
    )
    for method in methods:
        f = getattr(client.droplet_actions, method)
        with pytest.raises(NotImplementedError):
            f()
