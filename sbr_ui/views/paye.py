from flask import Blueprint, render_template, redirect, url_for


paye_bp = Blueprint('paye_bp', __name__, static_folder='static', template_folder='templates')


@paye_bp.route('/<id>', methods=['GET'])
def paye(id):
    return render_template('paye.html')