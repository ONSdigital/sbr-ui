from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user


login_bp = Blueprint('login_bp', __name__, static_folder='static', template_folder='templates')
logout_bp = Blueprint('logout_bp', __name__, static_folder='static', template_folder='templates')


@login_bp.route('/', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('search_bp.search'))
    return render_template('login.html', error=None)


@logout_bp.route('/Logout', methods=['POST'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect(url_for('login_bp.login'))
