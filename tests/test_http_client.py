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
        _ = client.account.info()

    assert str(e.value) == 'Unable to authenticate you'


@responses.activate
def test_bad_request(client):
    responses.add(
        responses.POST,
        'https://api.digitalocean.com/v2/droplets',
        json={'id': 'bad_request', 'message': 'Your request body was malformed.'},
        status=400,
    )

    with pytest.raises(client.BadRequest) as e:
        client.droplets.create('aaa', 'bbb', 'ccc', 'ddd')
    assert str(e.value) == 'Your request body was malformed.'


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


@responses.activate
def test_server_error(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account',
        json={'id': 'server_error', 'message': 'Internal server error.'},
        status=500,
    )

    with pytest.raises(client.ServerError) as e:
        _ = client.account.info()

    assert str(e.value) == 'Internal server error.'


@responses.activate
def test_rate_limit_exceeded(client):
    responses.add(
        responses.GET,
        'https://api.digitalocean.com/v2/account',
        json={'id': 'too_many_requests', 'message': 'API Rate limit exceeded.'},
        status=429,
    )

    with pytest.raises(client.RateLimitExceeded) as e:
        _ = client.account.info()

    assert str(e.value) == 'API Rate limit exceeded.'
