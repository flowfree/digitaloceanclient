import json

import pytest

import responses


@responses.activate
def test_list_all_images(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/images?page=2',
        json=load_json('image_list_p2.json')
    )
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/images',
        json=load_json('image_list_p1.json')
    )

    image_slugs = [i.slug for i in client.images.all()]
    expected_slugs = [
        'centos-6-x32',
        'centos-6-x64',
        'ubuntu-16-04-x32',
        'freebsd-12-x64',
        'rancheros',
        'ubuntu-18-04-x64',
        'fedora-32-x64',
        'centos-8-x64',
        'debian-10-x64',
        'debian-9-x64',
        'ubuntu-16-04-x64',
        'freebsd-11-x64-zfs',
        'fedora-31-x64',
        'ubuntu-20-04-x64',
        'freebsd-11-x64-ufs',
        'centos-7-x64',
        'freebsd-12-x64-zfs',
        'skaffolder-18-04',
        'izenda-18-04',
        'quickcorp-qcobjects-18-04',
        'fathom-18-04',
        'optimajet-workflowserver-18-04',
        'nimbella-18-04',
        'snapt-snaptaria-18-04',
        'snapt-snaptnova-18-04',
        'weconexpbx-7-6',
        'bitwarden-18-04',
        'buddy-18-04',
        'sharklabs-minecraftjavaedi-18-04',
        'selenoid-18-04',
        'litespeedtechnol-openlitespeednod-18-04',
        'simontelephonics-freepbx-7-6',
        'gluu-gluuserverce-18-04-3',
        'netfoundry-7-6',
        'kandralabs-zulip-18-04',
        'buddy-repman-18-04',
        'strapi-18-04',
        'wftutorials-purdm-18-04',
        'flipstarter-18-04',
        'caprover-18-04',
    ]

    assert image_slugs == expected_slugs


@responses.activate
def test_create_an_image(client, load_json):
    json_response = load_json('image_202_accepted.json')
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/images',
        json=json_response,
        status=202,
    )

    image = client.images.create(
        name='ubuntu-18.04-minimal',
        url='http://cloud-images.ubuntu.com/minimal/releases/'
            'bionic/release/ubuntu-18.04-minimal-cloudimg-amd64.img',
        region='nyc3',
        distribution='Ubuntu',
        description='Cloud-optimized image w/ small footprint',
        tags=['base-image', 'prod']
    )

    assert responses.calls[0].request.body.decode('utf-8') == json.dumps({
        'name': 'ubuntu-18.04-minimal',
        'url': 'http://cloud-images.ubuntu.com/minimal/releases/'
               'bionic/release/ubuntu-18.04-minimal-cloudimg-amd64.img',
        'region': 'nyc3',
        'distribution': 'Ubuntu',
        'description': 'Cloud-optimized image w/ small footprint',
        'tags': ['base-image', 'prod']
    })
    expected = json_response['image']
    assert image.id == expected['id']
    assert image.name == expected['name']
    assert image.distribution == expected['distribution']
    assert image.regions == expected['regions']
    assert image.created_at == expected['created_at']
    assert image.description == expected['description']
    assert image.tags == expected['tags']
    assert image.status == expected['status']
    assert image.error_message == expected['error_message']


@responses.activate
def test_retrieve_a_single_image(client, load_json):
    json_response = load_json('single_image.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/images/7555620',
        json=json_response,
    )

    image = client.images.get('7555620')

    expected = json_response['image']
    assert image.id == expected['id']
    assert image.name == expected['name']
    assert image.distribution == expected['distribution']
    assert image.slug == expected['slug']
    assert image.public == expected['public']
    assert image.regions == expected['regions']
    assert image.created_at == expected['created_at']
    assert image.min_disk_size == expected['min_disk_size']
    assert image.size_gigabytes == expected['size_gigabytes']
    assert image.description == expected['description']
    assert image.tags == expected['tags']
    assert image.status == expected['status']
    assert image.error_message == expected['error_message']


@responses.activate
def test_retrieve_an_image_by_slug(client, load_json):
    json_response = load_json('single_image.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/images/sample-snapshot',
        json=json_response,
    )

    image = client.images.get(slug='sample-snapshot')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'GET'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/images/sample-snapshot'

    expected = json_response['image']
    assert image.id == expected['id']
    assert image.name == expected['name']


@responses.activate
def test_retrieve_an_image_by_invalid_slug(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/images/xxxyyyzzz',
        json={'message': 'The requested image does not exist.'},
        status=404,
    )

    with pytest.raises(client.NotFound) as e:
        _ = client.images.get(slug='xxxyyyzzz')
    assert str(e.value) == 'NotFound: The requested image does not exist.'


@responses.activate
def test_update_an_image(client, load_json):
    json_response = load_json('single_image2.json')
    responses.add(
        responses.PUT,
        'https://api.digitalocean.com/v2/images/7555620',
        json=json_response,
        status=200
    )

    image = client.images.update('7555620', name='new-image-name')

    assert responses.calls[0].request.body.decode('utf-8') == \
           json.dumps({'name': 'new-image-name'})

    expected = json_response['image']
    assert image.id == expected['id']
    assert image.name == expected['name']
    assert image.distribution == expected['distribution']
    assert image.slug == expected['slug']
    assert image.public == expected['public']
    assert image.regions == expected['regions']
    assert image.created_at == expected['created_at']
    assert image.min_disk_size == expected['min_disk_size']
    assert image.size_gigabytes == expected['size_gigabytes']
    assert image.description == expected['description']
    assert image.tags == expected['tags']
    assert image.status == expected['status']
    assert image.error_message == expected['error_message']


@responses.activate
def test_delete_an_image(client):
    responses.add(
        responses.DELETE,
        'https://api.digitalocean.com/v2/images/7938391',
        status=204
    )

    response = client.images.delete('7938391')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.method == 'DELETE'
    assert responses.calls[0].request.url == \
           'https://api.digitalocean.com/v2/images/7938391'
    assert response is None
