from flask import Blueprint, render_template, redirect, url_for


vat_bp = Blueprint('vat_bp', __name__, static_folder='static', template_folder='templates')


@vat_bp.route('/<id>', methods=['GET'])
def vat(id):
    return render_template('vat.html')