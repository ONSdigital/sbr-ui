import logging
from structlog import wrap_logger
from flask import Blueprint, request, redirect, url_for, session
from flask_login import login_required

from sbr_ui.services.search_service import SearchService
from sbr_ui.models.exceptions import ApiError


logger = wrap_logger(logging.getLogger(__name__))


api_bp = Blueprint('api_bp', __name__, static_folder='static', template_folder='templates')


search_service = SearchService()


# Need to look at where to store these, for internationalisation etc.
ERROR_MESSAGES = {
    404: 'The search query you entered did not return any results.',
    500: 'An error occurred. Please contact your system administrator.',
    503: 'An error occurred. This is likely to be an issue with ElasticSearch.',
    504: 'An error occurred. This is likely to be a timeout issue.'
}

ERROR_CODES = {
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable',
    504: 'Gateway Timeout'
}


@api_bp.errorhandler(ApiError)
def handle_error(error: ApiError):
    error_code_detail = ERROR_CODES.get(error.status_code, 'Error')
    session['level'] = 'warn' if error.status_code == 404 else 'error'
    session['title'] = f'{error.status_code} - {error_code_detail}'
    session['error_message'] = ERROR_MESSAGES.get(error.status_code, 'An error occurred.')
    return redirect(url_for('error_bp.error'))


@api_bp.route('/periods/<period>/types/<unit_type>/units/<unit_id>', methods=['GET'])
@login_required
def get_unit_by_id(period, unit_type, unit_id):

    try:
        json = search_service.get_unit_by_id_type_period(unit_id, unit_type, period)
    except (ApiError, ValueError) as e:
        logger.error('Unable to return results for get unit by id')
        raise e

    filtered_children = format_children(json['children'])
    json['children'] = filtered_children
    session['business'] = json

    return redirect_to_unit_page(unit_type, unit_id)


@api_bp.route('/search_reference_number', methods=['POST', 'GET'])
@login_required
def search_reference_number():
    unit_id = request.form['ReferenceNumber']

    try:
        json = search_service.search_by_id(unit_id)
    except (ApiError, ValueError) as e:
        logger.error('Unable to return search results')
        raise e

    unit_type = json.get("unitType")
    formatted_children = format_children(json['children'])
    json['children'] = formatted_children
    session['business'] = json
    session['id'] = json.get("id")

    return redirect_to_unit_page(unit_type, unit_id)


def format_children(children: dict):
    vats = []
    chs = []
    payes = []
    leus = []

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

    children = {"VAT": vats, "CH": chs, "PAYE": payes, "LEU": leus}

    # Filter empty arrays
    return {k: v for k, v in children.items() if len(v) != 0}


def redirect_to_unit_page(unit_type: str, unit_id: str):
    if unit_type == "LEU":
        return redirect(url_for('leu_bp.leu', id=unit_id))
    elif unit_type == "VAT":
        return redirect(url_for('vat_bp.vat', id=unit_id))
    elif unit_type == "PAYE":
        return redirect(url_for('paye_bp.paye', id=unit_id))
    elif unit_type == "CH":
        return redirect(url_for('ch_bp.ch', id=unit_id))
    elif unit_type == "ENT":
        return redirect(url_for('ent_bp.ent', id=unit_id))