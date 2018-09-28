import logging

from flask import Blueprint, render_template, session


logger = logging.getLogger(__name__)
error_bp = Blueprint('error_bp', __name__, template_folder='templates/errors')


@error_bp.route('/', methods=['GET'])
def error():
    """
    This is a generic error handler for showing an error on a new page, using error information from
    either the session or defaults.
    """
    title = session.get('title', 'Error')
    error_message = session.get('error_message', 'An error has occurred.')
    level = session.get('level', 'error')
    return render_template('errors/error.html', title=title, error_message=error_message, level=level)

