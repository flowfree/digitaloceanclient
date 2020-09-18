import pytest
import responses 


@responses.activate
def test_unauthorized(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account',
        json={"id": "Unauthorized", "message": "Unable to authenticate you"},
        status=401
    )

    with pytest.raises(client.Unauthorized) as e:
        account = client.account.get()

    assert f'{e.value}' == 'Unable to authenticate you'
