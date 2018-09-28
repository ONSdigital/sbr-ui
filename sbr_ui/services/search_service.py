import logging
import requests
from structlog import wrap_logger
from typing import List, Tuple, Optional

from sbr_ui.models.exceptions import ApiError
from sbr_ui.utilities.helpers import log_api_error


logger = wrap_logger(logging.getLogger(__name__))


class SearchService:
    NumResults = Optional[int]
    Business = dict
    Businesses = List[Business]
    SearchResponse = Tuple[NumResults, Businesses]

    def __init__(self):
        self.base_url = 'http://localhost:9000'
        self.version = 'v1'

    def search_reference_number(self, reference_number: str) -> Business:
        response = requests.get(f'{self.base_url}/{self.version}/search/{reference_number}')

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            log_api_error(response.status_code, 'Failed to retrieve Business by reference number', reference_number)
            raise ApiError(response)

        return response.json()