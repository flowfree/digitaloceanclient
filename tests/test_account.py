import responses


@responses.activate
def test_get_current_account(client, load_json):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account',
        json=load_json('account.json')
    )

    account = client.account.info()

    assert account.uuid == 'c2b5a91622fbc5a2489c068eb6e53490c10baaf7'
    assert account.email == 'nash@example.com'
    assert account.email_verified == True
    assert account.droplet_limit == 25
    assert account.floating_ip_limit == 3
    assert account.volume_limit == 100


@responses.activate
def test_get_current_balance(client, load_json):
    json_response = load_json('account_balance.json')
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/customers/my/balance',
        json=json_response,
    )

    balance = client.account.balance()

    assert balance.month_to_date_balance == float(json_response['month_to_date_balance'])
    assert balance.account_balance == float(json_response['account_balance'])
    assert balance.month_to_date_usage == float(json_response['month_to_date_usage'])
    assert balance.generated_at == json_response['generated_at']
