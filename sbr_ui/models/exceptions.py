import logging
import sys

from structlog import wrap_logger


logger = wrap_logger(logging.getLogger(__name__))


class ApiError(Exception):
    """ We use ApiError to encapsulate any 400/404/500 etc. errors from an external API """
    def __init__(self, response):
        self.url = response.url
        self.status_code = response.status_code
        self.message = response.text


class InvalidEnvironment(Exception):
    """ An InvalidEnvironment exception will be thrown if anything other than DEV/TEST/PROD is passed in """
    def __init__(self, key):
        logger.error('Invalid Environment key used, should be DEV/TEST/PROD', key=key)
        sys.exit("Flask Application failed to start due to invalid environment variable")


class MissingEnvironmentVariable(Exception):
    """ A MissingEnvironmentVariable exception will be thrown if any of the required environment variables are
    missing. (This will only occur in PROD) """
    def __init__(self, missing_vars):
        logger.error('Missing environment variables', missing_vars=missing_vars)
        sys.exit("Flask Application failed to start due to missing required environment variables")
