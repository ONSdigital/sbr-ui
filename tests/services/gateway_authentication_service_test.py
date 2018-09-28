import pytest
import responses

from sbr_ui import ApiError
from sbr_ui.services.gateway_authentication_service import GatewayAuthenticationService


url = 'http://localhost:9000/login'
username = 'admin'
password = 'admin'
headers = {'content-type': 'application/json'}


@pytest.fixture
def auth():
    return GatewayAuthenticationService('http://localhost:9000/login')

@responses.activate
def test_login_success(auth):
    responses.add(responses.POST, url, json={"token": "12345", "role": "admin"}, status=200, headers=headers)
    token, role = auth.login(username, password)
    assert token == "12345"
    assert role == "admin"

@responses.activate
def test_login_unauthorized(auth):
    responses.add(responses.POST, url, status=401, headers=headers)
    with pytest.raises(ApiError) as err:
        auth.login(username, password)
    assert err.value.status_code == 401
    assert err.value.url == url

@responses.activate
def test_login_server_error(auth):
    responses.add(responses.POST, url, status=500, headers=headers)
    with pytest.raises(ApiError) as err:
        auth.login(username, password)
    assert err.value.status_code == 500
    assert err.value.url == url

@responses.activate
def test_login_invalid_json(auth):
    responses.add(responses.POST, url, status=200, json={"admin": "role", "12345": "token"}, headers=headers)
    with pytest.raises(ValueError):
        auth.login(username, password)