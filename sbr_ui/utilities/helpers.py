import logging
import base64
from structlog import wrap_logger
from functools import reduce

from sbr_ui.utilities.sic_codes import industry_code_description
from sbr_ui.utilities.convert_bands import employment_bands, legal_status_bands, turnover_bands, trading_status_bands


logger = wrap_logger(logging.getLogger(__name__))


def compose(*fns):
    """ https://mathieularose.com/function-composition-in-python/ """
    return reduce(lambda g, f: lambda x: f(g(x)), fns, lambda x: x)


def acronym_to_sbr_api_format(acronym):
    return {'ENT': 'ents', 'LEU': 'leus', 'LU': 'lous', 'VAT': 'vats', 'PAYE': 'payes', 'CH': 'crns'}.get(acronym)


def convert_band(unit: dict, key: str, not_found_key: str, bands: dict) -> dict:
    initial_value = unit.get(key)

    # If the key isn't valid then just return the original unit dict
    if initial_value is None:
        return unit
    else:
        not_found_msg = f'No {not_found_key} could be found'
        description = bands.get(initial_value, not_found_msg)
        return {**unit, key: f'{initial_value} - {description}'}


def log_api_error(status: int, error_msg: str, query: str):
    """ Depending on the severity of the response, log at an appropriate level """
    if status in [400, 401, 404]:
        logger.info(error_msg, status=status, query=query)
    elif status == 500:
        logger.error(error_msg, status=status, query=query)


def base_64_encode(to_encode: str) -> str:
    """ Encode a string using base64, for Basic Authentication """
    return base64.b64encode(to_encode.encode())


def format_children(children: dict):
    """ TODO: do this immutably """
    vats = []
    chs = []
    payes = []
    leus = []
    lus = []

    # Rather than a dict of unitId:unitType, we want a dict of unitType:[unitId's], to make parsing them in the
    # template easier
    for child_id, child_type in children.items():
        if child_type == "VAT":
            vats.append(child_id)
        elif child_type == "CH":
            chs.append(child_id)
        elif child_type == "PAYE":
            payes.append(child_id)
        elif child_type == "LEU":
            leus.append(child_id)
        elif child_type == "LU":
            lus.append(child_id)

    children = {"VAT": vats, "CH": chs, "PAYE": payes, "LEU": leus, "LU": lus}

    # Filter empty arrays
    return {k: v for k, v in children.items() if len(v) != 0}


sic = lambda unit: convert_band(unit, 'industryCode', 'industry code description', industry_code_description)
sic07 = lambda unit: convert_band(unit, 'sic07', 'industry code description', industry_code_description)
trading_status = lambda unit: convert_band(unit, 'tradingStatus', 'trading status', trading_status_bands)
legal_status = lambda unit: convert_band(unit, 'legalStatus', 'legal status', legal_status_bands)
employment_band = lambda unit: convert_band(unit, 'employmentBands', 'employment band', employment_bands)
turnover_band = lambda unit: convert_band(unit, 'turnover', 'turnover band', turnover_bands)

convert_bands = compose(sic, sic07, trading_status, legal_status, employment_band, turnover_band)
