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
