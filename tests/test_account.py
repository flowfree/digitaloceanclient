import responses


@responses.activate
def test_get_current_account(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account',
        json=load_json('account.json')
    )

    account = client.account.get()

    assert account.uuid == 'c2b5a91622fbc5a2489c068eb6e53490c10baaf7'
    assert account.email == 'nash@example.com'
    assert account.email_verified == True
    assert account.droplet_limit == 25
    assert account.floating_ip_limit == 3
    assert account.volume_limit == 100
