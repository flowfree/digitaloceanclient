from digitaloceanclient.models import Account


def test_load_from_json():
    data = {
        "droplet_limit": 25,
        "floating_ip_limit": 5,
        "volume_limit": 10,
        "email": "sammy@digitalocean.com",
        "uuid": "b6fr89dbf6d9156cace5f3c78dc9851d957381ef",
        "email_verified": True,
        "status": "active",
        "status_message": ""
    }

    account = Account(data)

    assert account.uuid == 'b6fr89dbf6d9156cace5f3c78dc9851d957381ef'
    assert account.email == 'sammy@digitalocean.com'
    assert account.droplet_limit == 25
    assert account.floating_ip_limit == 5
    assert account.volume_limit == 10
    assert account.email_verified == True
    assert account.status == Account.STATUS_ACTIVE
    assert account.status_message == ''
