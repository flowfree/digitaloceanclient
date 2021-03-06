from digitaloceanclient.models import SSHKey


def test_load_from_json():
    data = {
        "id": 512189,
        "fingerprint": "3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa",
        "public_key": "ssh-rsa AEXAMPLEaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example",
        "name": "My SSH Public Key"
    }

    ssh_key = SSHKey(data)

    assert ssh_key.id == data['id']
    assert ssh_key.fingerprint == data['fingerprint']
    assert ssh_key.public_key == data['public_key']
    assert ssh_key.name == data['name']
