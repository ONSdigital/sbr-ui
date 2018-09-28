from flask import Blueprint, render_template, redirect, url_for


leu_bp = Blueprint('leu_bp', __name__, static_folder='static', template_folder='templates')


@leu_bp.route('/<id>', methods=['GET'])
def leu(id):
    return render_template('leu.html')