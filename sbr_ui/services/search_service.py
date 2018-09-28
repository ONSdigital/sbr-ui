import logging
import requests
from structlog import wrap_logger

from sbr_ui.models.exceptions import ApiError
from sbr_ui.utilities.helpers import log_api_error
from sbr_ui.utilities.helpers import acronym_to_sbr_api_format


logger = wrap_logger(logging.getLogger(__name__))


class SearchService:
    Unit = dict

    def __init__(self):
        self.base_url = 'http://localhost:9000'
        self.version = 'v1'

    def search_by_id(self, unit_id: str) -> Unit:
        url = f'{self.base_url}/{self.version}/search/{unit_id}'
        logger.info("Sending search by id request", url=url)
        response = requests.get(url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to retrieve Unit by id', url)
            raise ApiError(response)

        return response.json()


    def get_unit_by_id_type_period(self, unit_id: str, unit_type: str, period: str) -> Unit:
        formatted_unit_type = acronym_to_sbr_api_format(unit_type)
        url = f'{self.base_url}/{self.version}/periods/{period}/{formatted_unit_type}/{unit_id}'
        logger.info("Sending get by id, unit type and period request", url=url)
        response = requests.get(url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to retrieve Unit by id, type and period', url)
            raise ApiError(response)

        return response.json()
