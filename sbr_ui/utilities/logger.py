import logging
from structlog import wrap_logger


logger = wrap_logger(logging.getLogger(__name__))


def initialise_logger(config):
    log_level = config['LOG_LEVEL']
    logging.basicConfig(level=log_level, format='%(message)s')
    logger.info('Log level set', log_level=log_level)