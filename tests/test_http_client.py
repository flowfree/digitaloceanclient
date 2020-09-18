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


@responses.activate
def test_not_found(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/droplets/12345',
        json={'id': 'not_found', 'message': 'The resource you were accessing could not be found.'},
        status=404,
    )

    with pytest.raises(client.NotFound) as e:
        _ = client.droplets.get(12345)

    assert str(e.value) == 'The resource you were accessing could not be found.'

