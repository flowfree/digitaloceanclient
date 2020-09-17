import responses


@responses.activate
def test_list_all_sizes(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/sizes',
        json=load_json('size_list.json')
    )

    rows = client.sizes.all()

    size = next(rows)
    assert size.slug == 's-1vcpu-1gb'
    assert size.memory == 1024
    assert size.vcpus == 1
    assert size.disk == 25
    assert size.transfer == 1.0
    assert size.price_monthly == 5.0
    assert size.price_hourly == 0.00744
    assert size.regions == [
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1"
    ]
    assert size.available == True

    size = next(rows)
    assert size.slug == '512mb'
    assert size.memory == 512
    assert size.vcpus == 1
    assert size.disk == 20
    assert size.transfer == 1.0
    assert size.price_monthly == 5.0
    assert size.price_hourly == 0.00744
    assert size.regions == [
        "ams2",
        "ams3",
        "blr1",
        "fra1",
        "lon1",
        "nyc1",
        "nyc2",
        "nyc3",
        "sfo1",
        "sfo2",
        "sfo3",
        "sgp1",
        "tor1"
    ]
    assert size.available == True
