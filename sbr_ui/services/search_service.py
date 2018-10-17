import logging
import requests
from structlog import wrap_logger

from flask import current_app

from sbr_ui.models.exceptions import ApiError
from sbr_ui.utilities.helpers import log_api_error
from sbr_ui.utilities.helpers import acronym_to_sbr_api_format


logger = wrap_logger(logging.getLogger(__name__))


class SearchService:
    Unit = dict

    @staticmethod
    def search_by_id(unit_id: str) -> Unit:
        base_url = current_app.config['API_URL']
        timeout = current_app.config['API_TIMEOUT']
        url = f'{base_url}/v1/search/{unit_id}'
        logger.info("Sending search by id request", url=url)
        response = requests.get(url, timeout=timeout)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to retrieve Unit by id', url)
            raise ApiError(response)

        return response.json()

    @staticmethod
    def get_unit_by_id_type_period(unit_id: str, unit_type: str, period: str) -> Unit:
        base_url = current_app.config['API_URL']
        timeout = current_app.config['API_TIMEOUT']
        formatted_unit_type = acronym_to_sbr_api_format(unit_type)
        url = f'{base_url}/v1/periods/{period}/{formatted_unit_type}/{unit_id}'
        logger.info("Sending get by id, unit type and period request", url=url)
        response = requests.get(url, timeout=timeout)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to retrieve Unit by id, type and period', url)
            raise ApiError(response)

        return response.json()
