import logging
import requests
from structlog import wrap_logger
from typing import Tuple

from sbr_ui.models.exceptions import ApiError
from sbr_ui.utilities.helpers import log_api_error, base_64_encode


logger = wrap_logger(logging.getLogger(__name__))


class GatewayAuthenticationService:
    Role = str
    Token = str  # A uuid from the API Gateway
    TokenAndRole = Tuple[Token, Role]

    def __init__(self, gateway_auth_url: str):
        self.gateway_auth_url = gateway_auth_url

    def login(self, username: str, password: str) -> TokenAndRole:
        logger.debug("Logging user in", username=username)
        headers = {'content-type': 'application/json', 'Authorization': str(base_64_encode(f'{username}:{password}'))}
        response = requests.post(self.gateway_auth_url, headers=headers)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to authorize via the API Gateway', self.gateway_auth_url)
            raise ApiError(response)

        # Potentially need to throw an exception here if we don't get back a token or role
        # Also, potentially need to match the BusinessService in terms of returning the response.json()
        try:
            json = response.json()
        except ValueError:
            logger.error("Invalid Gateway response JSON, unable to parse")
            raise ValueError(response)

        token = json.get('token')
        role = json.get('role')

        if token is None or role is None:
            logger.error("Returned Gateway JSON is in the wrong format")
            raise ValueError(response)

        return token, role
