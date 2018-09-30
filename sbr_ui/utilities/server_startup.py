import logging
import os

from structlog import wrap_logger

from test_data import units
from sbr_ui import InvalidEnvironment, MissingEnvironmentVariable
from sbr_ui.services.search_service import SearchService
from sbr_ui.services.fake_search_service import FakeSearchService


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


def initialise_search_service():
    # TODO: find way of using config here rather than accessing environment variables again
    if os.environ['USE_FAKE_DATA']:
        logger.debug("USE_FAKE_DATA set to true, using test data", test_data=units)
        return FakeSearchService
    return SearchService
