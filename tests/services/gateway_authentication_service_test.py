import pytest
import responses

from sbr_ui import create_application
from sbr_ui import ApiError
from sbr_ui.services.gateway_authentication_service import GatewayAuthenticationService


url = 'http://localhost:9000'
username = 'admin'
password = 'admin'
headers = {'content-type': 'application/json'}


@pytest.fixture
def auth():
    return GatewayAuthenticationService

@pytest.fixture
def app():
    app = create_application()
    app.config.update(AUTH_URL=url)
    return app

@responses.activate
def test_login_success(auth, app):
    responses.add(responses.POST, url, json={"token": "12345", "role": "admin"}, status=200, headers=headers)
    with app.app_context():
        token, role = auth.login(username, password)
    assert token == "12345"
    assert role == "admin"

@responses.activate
def test_login_unauthorized(auth, app):
    responses.add(responses.POST, url, status=401, headers=headers)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            auth.login(username, password)
    assert err.value.status_code == 401
    assert err.value.url == f'{url}/'

@responses.activate
def test_login_server_error(auth, app):
    responses.add(responses.POST, url, status=500, headers=headers)
    with app.app_context():
        with pytest.raises(ApiError) as err:
            auth.login(username, password)
    assert err.value.status_code == 500
    # For some reason, a trailing '/' is added to the URL
    assert err.value.url == f'{url}/'

@responses.activate
def test_login_invalid_json(auth, app):
    responses.add(responses.POST, url, status=200, json={"admin": "role", "12345": "token"}, headers=headers)
    with app.app_context():
        with pytest.raises(ValueError):
            auth.login(username, password)