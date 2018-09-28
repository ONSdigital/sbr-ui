from flask import Blueprint, render_template
from flask_login import login_required


home_bp = Blueprint('home_bp', __name__, static_folder='static', template_folder='templates')


@home_bp.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html')