import logging
import base64
from structlog import wrap_logger
from functools import reduce


logger = wrap_logger(logging.getLogger(__name__))


# https://mathieularose.com/function-composition-in-python/
def compose(*fns):
    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)


def convert_band(business: dict, key: str, not_found_key: str, bands: dict) -> dict:
    initial_value = business[key]
    not_found_msg = f'No {not_found_key} could be found.'
    description = bands.get(initial_value, not_found_msg)
    return {**business, key: f'{initial_value} - {description}'}


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
