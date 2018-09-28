from flask import Blueprint, render_template, redirect, url_for, session


ent_bp = Blueprint('ent_bp', __name__, static_folder='static', template_folder='templates')
lu_bp = Blueprint('lu_bp', __name__, static_folder='static', template_folder='templates')
leu_bp = Blueprint('leu_bp', __name__, static_folder='static', template_folder='templates')
ch_bp = Blueprint('ch_bp', __name__, static_folder='static', template_folder='templates')
paye_bp = Blueprint('paye_bp', __name__, static_folder='static', template_folder='templates')
vat_bp = Blueprint('vat_bp', __name__, static_folder='static', template_folder='templates')


@ent_bp.route('/periods/<period>/types/ENT/units/<id>', methods=['GET'])
def ent(id, period):
    return render_template('ent.html')


@lu_bp.route('/periods/<period>/types/LU/units/<id>', methods=['GET'])
def lu(id, period):
    return render_template('lu.html')


@leu_bp.route('/periods/<period>/types/LEU/units/<id>', methods=['GET'])
def leu(id, period):
    return render_template('leu.html')


@ch_bp.route('/periods/<period>/types/CH/units/<id>', methods=['GET'])
def ch(id, period):
    return render_template('ch.html')


@paye_bp.route('/periods/<period>/types/PAYE/units/<id>', methods=['GET'])
def paye(id, period):
    return render_template('paye.html')


@vat_bp.route('/periods/<period>/types/VAT/units/<id>', methods=['GET'])
def vat(id, period):
    return render_template('vat.html')