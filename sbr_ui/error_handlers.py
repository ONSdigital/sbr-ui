from flask import redirect, url_for, session
import requests
from sbr_ui import app


"""
Generic errors are handled here, specific errors for the API are handled within the API blueprint.
"""


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
