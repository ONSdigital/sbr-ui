from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


login_bp = Blueprint('login_bp', __name__, static_folder='static', template_folder='templates')


@login_bp.route('/', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.home'))
    return render_template('login.html', error=None)
