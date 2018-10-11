import uuid

from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import current_user, login_required, logout_user, login_user

from sbr_ui.models.user import User, users
from sbr_ui.services.gateway_authentication_service import GatewayAuthenticationService

authentication_bp = Blueprint('authentication_bp', __name__, static_folder='static', template_folder='templates')


@authentication_bp.route('/', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('search_bp.search'))
    return redirect(url_for('authentication_bp.login'))


@authentication_bp.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('search_bp.search'))
        return render_template('login.html', error=None)

    username = request.form['username']
    password = request.form['password']

    # If we are in PROD, we need to authenticate via the API Gateway
    if current_app.config['ENVIRONMENT'] == 'PROD':
        token, role = GatewayAuthenticationService.login(username, password)
        user_id = str(uuid.uuid4())
        user = User(user_id, token, role)
        login_user(user)
        users.append(user)
        return redirect(url_for('search_bp.search'))
    else:
        if username == 'admin' and password == 'admin':
            user_id = str(uuid.uuid4())
            user = User(user_id, str(uuid.uuid4()), 'admin')
            login_user(user)
            users.append(user)
            return redirect(url_for('search_bp.search'))
        else:
            flash('Invalid Credentials. Please try again.')
            return render_template('login.html')


@authentication_bp.route('/Logout', methods=['POST'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect(url_for('authentication_bp.login'))
