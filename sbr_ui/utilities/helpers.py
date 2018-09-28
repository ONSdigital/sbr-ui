import logging
import base64
from structlog import wrap_logger
from functools import reduce


logger = wrap_logger(logging.getLogger(__name__))


# https://mathieularose.com/function-composition-in-python/
def compose(*fns):
    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)


def convert_band(unit: dict, key: str, not_found_key: str, bands: dict) -> dict:
    logger.error("convert_band", unit=unit, key=key, not_found_key=not_found_key, bands=bands)
    initial_value = unit.get(key)
    if initial_value is None:
        return unit
    else:
        not_found_msg = f'No {not_found_key} could be found.'
        description = bands.get(initial_value, not_found_msg)
        return {**unit, key: f'{initial_value} - {description}'}


def log_api_error(status: int, error_msg: str, query: str):
    """ Depending on the severity of the response, log at an appropriate level """
    if status == 401:
        logger.info(error_msg, status=status, query=query)
    if status == 404:
        logger.info(error_msg, status=status, query=query)
    elif status == 400:
        logger.warning(error_msg, status=status, query=query)
    elif status == 500:
        logger.error(error_msg, status=status, query=query)


def base_64_encode(to_encode: str) -> str:
    """ Encode a something using base64, for Basic Authentication """
    return base64.b64encode(to_encode.encode())

# {'id': '1', 'unitType': 'ENT', 'period': '201810', 'children': {'VAT': ['6'], 'CH': ['4'], 'PAYE': ['5'], 'LEU': ['2'], 'LU': ['3']}, 'vars': {'ern': '918237891237', 'entref': '879372942', 'name': 'Tesco', 'tradingStyle': '3', 'sic07': '10000', 'legalStatus': '1', 'employees': '68', 'jobs': '1038', 'turnover': 'A', 'prn': '0387', 'workingProprietors': '8', 'employment': 'A', 'region': 'Gwent', 'address': {'line1': '6 Big House', 'line2': 'Long Street', 'line3': 'Newport', 'line4': 'South Wales', 'line5': 'Wales', 'postcode': 'NP20 ABC'}}}
