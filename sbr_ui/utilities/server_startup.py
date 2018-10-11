import logging
import os

from structlog import wrap_logger

from sbr_ui.models.exceptions import InvalidEnvironment, MissingEnvironmentVariable


logger = wrap_logger(logging.getLogger(__name__))


def get_and_validate_environment():
    env = os.getenv('ENVIRONMENT')
    if env not in ['DEV', 'TEST', 'PROD']:
        raise InvalidEnvironment(env)
    return env


def check_required_environment_variables_present(env, config):
    """ If we are in PROD, we want to fail fast if any config is missing """
    if env == 'PROD':
        missing_vars = [var for var in config['REQUIRED_VARS'] if config.get(var) is None]
        if missing_vars:
            raise MissingEnvironmentVariable(missing_vars)
