from flask import Blueprint, render_template, redirect, url_for


ch_bp = Blueprint('ch_bp', __name__, static_folder='static', template_folder='templates')


@ch_bp.route('/<id>', methods=['GET'])
def ch(id):
    return render_template('ch.html')