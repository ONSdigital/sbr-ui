import logging
import requests
from structlog import wrap_logger


logger = wrap_logger(logging.getLogger(__name__))


class FakeSearchService():
    Unit = dict

    def __init__(self, units):
        self.units = units

    def search_by_id(self, unit_id: str) -> Unit:
        logger.info("Searching test data by unit id", unit_id=unit_id)

        matches = list(filter(lambda x: x["id"] == unit_id, self.units))
        if len(matches) > 0:
            return matches[0].copy()
        else:
            raise requests.exceptions.HTTPError("Not Found", 404)

    def get_unit_by_id_type_period(self, unit_id: str, unit_type: str, period: str) -> Unit:
        logger.info("Searching test data by unit id, unit type and period", unit_id=unit_id, unit_type=unit_type, period=period)
        matches = list(filter(lambda x:
                              x["id"] == unit_id and
                              x["period"] == period and
                              x["unitType"] == unit_type, self.units))

        if len(matches) > 0:
            return matches[0].copy()
        else:
            raise requests.exceptions.HTTPError("Not Found", 404)
