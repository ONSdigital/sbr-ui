import uuid
import logging
from structlog import wrap_logger
from flask import Blueprint, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user, logout_user, login_user

from sbr_ui import app
from sbr_ui.models.exceptions import ApiError
from sbr_ui.models.user import User, users
from sbr_ui.services.gateway_authentication_service import GatewayAuthenticationService


logger = wrap_logger(logging.getLogger(__name__))


authentication_bp = Blueprint('authentication_bp', __name__, static_folder='static', template_folder='templates')


authentication_service = GatewayAuthenticationService(app.config['AUTH_URL'])


@authentication_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # If we are in PROD, we need to authenticate via the API Gateway
    if app.config['ENVIRONMENT'] == 'PROD':
        try:
            token, role = authentication_service.login()
        except (ApiError, ValueError) as e:
            logger.warning('Unable to authenticate via the API Gateway')
            raise e
        user_id = str(uuid.uuid4())
        user = User(user_id, token, role)
        login_user(user)
        users.append(user)
        return redirect(url_for('home_bp.home'))
    else:
        if username == 'admin' and password == 'admin':
            user_id = str(uuid.uuid4())
            user = User(user_id, str(uuid.uuid4()), 'admin')
            login_user(user)
            users.append(user)
            return redirect(url_for('home_bp.home'))
        else:
            flash('Invalid Credentials. Please try again.')
            return redirect(url_for('login_bp.login'))


@authentication_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect(url_for('login_bp.login'))
