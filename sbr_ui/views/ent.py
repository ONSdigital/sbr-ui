from flask import Blueprint, render_template, redirect, url_for, session


ent_bp = Blueprint('ent_bp', __name__, static_folder='static', template_folder='templates')


@ent_bp.route('/<id>', methods=['GET'])
def ent(id):
    return render_template('ent.html')