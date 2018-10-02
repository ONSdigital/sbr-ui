import logging

import requests
from structlog import wrap_logger

from flask import Flask, redirect, request, url_for, session
from flask_login import LoginManager
from flask_session import Session

from sbr_ui.models.user import User, users
from sbr_ui.routes.authentication import authentication_bp
from sbr_ui.routes.errors import error_bp
from sbr_ui.routes.unit_pages import search_bp, unit_pages_bp
from sbr_ui.utilities.logger import initialise_logger
from sbr_ui.utilities.server_startup import get_and_validate_environment, check_required_environment_variables_present


logger = wrap_logger(logging.getLogger(__name__))


def create_application():
    app = Flask(__name__)

    environment = get_and_validate_environment()
    formatted_env = environment.lower().title()  # DEV -> Dev, use same format as class name

    app_config_path = f'config.{formatted_env}Config'
    app.config.from_object(app_config_path)

    log_level = app.config['LOG_LEVEL']
    logging.basicConfig(level=log_level, format='%(message)s')
    logger.info('Log level set', log_level=log_level)

    check_required_environment_variables_present(environment, app.config)
    initialise_logger(app.config)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.url_map.strict_slashes = False
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    app.register_blueprint(authentication_bp, url_prefix='/')
    app.register_blueprint(error_bp, url_prefix='/Error')
    app.register_blueprint(search_bp)
    app.register_blueprint(unit_pages_bp, url_prefix='/Search')

    @app.errorhandler(404)
    @app.errorhandler(requests.exceptions.HTTPError)
    def not_found_error(error):
        session['level'] = 'warn'
        session['title'] = '404 - Not Found'
        session['error_message'] = 'The URL you have navigated to cannot be found.'
        return redirect(url_for('error_bp.error'))

    @app.errorhandler(401)
    def not_authenticated_error(error):
        session['level'] = 'error'
        session['title'] = '401 - Not Authenticated'
        session['error_message'] = 'Please login before navigating to the Home or Results pages.'
        return redirect(url_for('error_bp.error'))

    @login_manager.user_loader
    def load_user(user_id) -> User:
        maybe_user = next((user for user in users if user.id == user_id), None)
        return maybe_user

    @app.before_request
    def clear_trailing():
        """ Remove trailing slashes: https://stackoverflow.com/a/40365514 """
        rp = request.path
        if rp != '/' and rp.endswith('/'):
            return redirect(rp[:-1])

    return app