import logging
import requests
from structlog import wrap_logger
from typing import Tuple
from flask import current_app

from sbr_ui.models.exceptions import ApiError
from sbr_ui.utilities.helpers import log_api_error, base_64_encode


logger = wrap_logger(logging.getLogger(__name__))


class GatewayAuthenticationService:
    Role = str
    Token = str  # A uuid from the API Gateway
    TokenAndRole = Tuple[Token, Role]

    @staticmethod
    def login(username: str, password: str) -> TokenAndRole:
        gateway_auth_url = current_app.config['AUTH_URL']
        logger.debug("Logging user in", username=username)
        headers = {'content-type': 'application/json', 'Authorization': str(base_64_encode(f'{username}:{password}'))}
        response = requests.post(gateway_auth_url, headers=headers)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to authorize via the API Gateway', gateway_auth_url)
            raise ApiError(response)

        json = response.json()
        token = json.get('token')
        role = json.get('role')

        if token is None or role is None:
            logger.error("Returned Gateway JSON is in the wrong format")
            raise ValueError(response)

        return token, role
