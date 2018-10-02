import logging
from structlog import wrap_logger
from flask import Blueprint, render_template, session, request, redirect, url_for
from flask_login import login_required

from sbr_ui import get_search_service, app
from sbr_ui.utilities.helpers import format_children, convert_bands

logger = wrap_logger(logging.getLogger(__name__))


unit_pages_bp = Blueprint('unit_pages_bp', __name__, static_folder='static', template_folder='templates')
search_bp = Blueprint('search_bp', __name__, static_folder='static', template_folder='templates')


search_service = get_search_service(app.config)


@search_bp.route('/Search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'GET':
        return render_template('search.html')
    unit_id = request.form['UnitId']
    json = search_service.search_by_id(unit_id)
    json_with_converted_bands = {**json, 'vars': convert_bands(json['vars'])}
    period = json_with_converted_bands['period']
    unit_type = json_with_converted_bands['unitType']
    session['json'] = json_with_converted_bands
    return redirect_to_unit_page(unit_id, unit_type, period)


@unit_pages_bp.route('/periods/<period>/types/ENT/units/<unit_id>', methods=['GET'])
@login_required
def ent(unit_id, period):
    json = get_json_from_session_or_api(unit_id, 'ENT', period)
    formatted_json = {**json, 'children': format_children(json['children'])}
    return render_template('ent.html', json=formatted_json)


@unit_pages_bp.route('/periods/<period>/types/LEU/units/<unit_id>', methods=['GET'])
@login_required
def leu(unit_id, period):
    json = get_json_from_session_or_api(unit_id, 'LEU', period)
    formatted_json = {**json, 'children': format_children(json['children'])}
    return render_template('leu.html', json=formatted_json)


@unit_pages_bp.route('/periods/<period>/types/LU/units/<unit_id>', methods=['GET'])
@login_required
def lu(unit_id, period):
    json = get_json_from_session_or_api(unit_id, 'LU', period)
    return render_template('lu.html', json=json)


@unit_pages_bp.route('/periods/<period>/types/CH/units/<unit_id>', methods=['GET'])
@login_required
def ch(unit_id, period):
    json = get_json_from_session_or_api(unit_id, 'CH', period)
    return render_template('ch.html', json=json)


@unit_pages_bp.route('/periods/<period>/types/PAYE/units/<unit_id>', methods=['GET'])
@login_required
def paye(unit_id, period):
    json = get_json_from_session_or_api(unit_id, 'PAYE', period)
    return render_template('paye.html', json=json)


@unit_pages_bp.route('/periods/<period>/types/VAT/units/<unit_id>', methods=['GET'])
@login_required
def vat(unit_id, period):
    json = get_json_from_session_or_api(unit_id, 'VAT', period)
    return render_template('vat.html', json=json)


def get_json_from_session_or_api(unit_id, unit_type, period):
    if session.get('json'):
        json = session['json']
        session.pop('json', None)
        return json
    else:
        json = search_service.get_unit_by_id_type_period(unit_id, unit_type, period)
        return {**json, 'vars': convert_bands(json['vars'])}


def redirect_to_unit_page(unit_id, unit_type, period):
    if unit_type == "LEU":
        return redirect(url_for('unit_pages_bp.leu', unit_id=unit_id, period=period))
    elif unit_type == "VAT":
        return redirect(url_for('unit_pages_bp.vat', unit_id=unit_id, period=period))
    elif unit_type == "PAYE":
        return redirect(url_for('unit_pages_bp.paye', unit_id=unit_id, period=period))
    elif unit_type == "CH":
        return redirect(url_for('unit_pages_bp.ch', unit_id=unit_id, period=period))
    elif unit_type == "ENT":
        return redirect(url_for('unit_pages_bp.ent', unit_id=unit_id, period=period))
    elif unit_type == "LU":
        return redirect(url_for('unit_pages_bp.lu', unit_id=unit_id, period=period))
