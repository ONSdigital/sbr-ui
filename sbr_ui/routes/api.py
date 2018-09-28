import logging
from structlog import wrap_logger
from flask import Blueprint, request, redirect, url_for, session
from flask_login import login_required
from sbr_ui import app # For some reason, current_app won't work to get the config
from sbr_ui.services.fake_search_service import FakeSearchService
from sbr_ui.services.search_service import SearchService
from sbr_ui.models.exceptions import ApiError
from sbr_ui.utilities.helpers import convert_bands, format_children


logger = wrap_logger(logging.getLogger(__name__))


if app.config.get('USE_FAKE_DATA'):
    logger.warn("USE_FAKE_DATA set to true, using test data")
    search_service = FakeSearchService()
else:
    search_service = SearchService()


api_bp = Blueprint('api_bp', __name__, static_folder='static', template_folder='templates')


@api_bp.route('/periods/<period>/types/<unit_type>/units/<unit_id>', methods=['GET'])
@login_required
def get_unit_by_id(period, unit_type, unit_id):

    try:
        json = search_service.get_unit_by_id_type_period(unit_id, unit_type, period)
    except (ApiError, ValueError) as e:
        logger.error("Unable to return results for get unit by id", unit_id=unit_id, unit_type=unit_type, period=period)
        raise e

    if unit_type in ["ENT", "LEU"]:
        filtered_children = format_children(json['children'])
        json['children'] = filtered_children

    json_with_band_conversion = convert_bands(json['vars'])

    json['vars'] = json_with_band_conversion
    session['business'] = json
    period = json.get("period")

    return redirect_to_unit_page(unit_type, unit_id, period)


@api_bp.route('/search_reference_number', methods=['POST', 'GET'])
@login_required
def search_reference_number():
    unit_id = request.form['ReferenceNumber']

    try:
        json = search_service.search_by_id(unit_id)
    except (ApiError, ValueError) as e:
        logger.error('Unable to return search results for reference number search', unit_id=unit_id)
        raise e

    unit_type = json.get("unitType")
    period = json.get("period")

    if unit_type in ["ENT", "LEU"]:
        filtered_children = format_children(json['children'])
        json['children'] = filtered_children


    json_with_band_conversion = convert_bands(json['vars'])

    json['vars'] = json_with_band_conversion
    session['business'] = json
    session['id'] = json.get("id")

    return redirect_to_unit_page(unit_type, unit_id, period)


def redirect_to_unit_page(unit_type: str, unit_id: str, period: str):
    if unit_type == "LEU":
        return redirect(url_for('leu_bp.leu', id=unit_id, period=period))
    elif unit_type == "VAT":
        return redirect(url_for('vat_bp.vat', id=unit_id, period=period))
    elif unit_type == "PAYE":
        return redirect(url_for('paye_bp.paye', id=unit_id, period=period))
    elif unit_type == "CH":
        return redirect(url_for('ch_bp.ch', id=unit_id, period=period))
    elif unit_type == "ENT":
        return redirect(url_for('ent_bp.ent', id=unit_id, period=period))
    elif unit_type == "LU":
        return redirect(url_for('lu_bp.lu', id=unit_id, period=period))