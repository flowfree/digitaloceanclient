import json 

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


@responses.activate
def test_create_new_tag(client, load_json):
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/tags',
        json=load_json('tag_201_created.json'),
        status=201
    )

    tag = client.tags.create(name='awesome')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/tags'
    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'name': 'awesome'
    })

    assert tag.name == 'awesome'
    assert tag.resources.count == 0


@responses.activate
def test_delete_tag(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/tags/sampletag',
        status=204
    )

    response = client.tags.delete(name='sampletag')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == 'https://api.digitalocean.com/v2/tags/sampletag'
    assert response == None
