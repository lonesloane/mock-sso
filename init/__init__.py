import os
import logging
from logging.handlers import TimedRotatingFileHandler

SSO_SERVICE_HOST = os.environ.get("SSO_SERVICE_HOST", "0.0.0.0")
SSO_SERVICE_PORT = os.environ.get("SSO_SERVICE_PORT", "8086")

LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')
LOG_FILE = os.environ.get('LOG_FILE', "./logs/mock-SSO.log")

# Set appropriate logging level
logging_level = getattr(logging, LOGGING_LEVEL.upper(), None)
if not isinstance(logging_level, int):
    raise ValueError('Invalid log level: %s' % LOGGING_LEVEL)
logger = logging.getLogger(__name__)
logger.setLevel(logging_level)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

# create file handler
fh = TimedRotatingFileHandler(filename=LOG_FILE, when='D', interval=1, backupCount=30)

fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

_log_level = 1  # verbosity of log. 1:debug - 2:verbose - 3:visual

logger.info('Logging object initialized with log level {level}'.format(level=_log_level))