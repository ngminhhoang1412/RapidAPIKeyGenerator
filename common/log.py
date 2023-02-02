import sys
import logging
import logging.handlers
import common.constants as Constant
from datetime import *

logger = logging.getLogger(__name__)


def log_error(exception, is_critical=False):
    if is_critical:
        logger.critical(exception, exc_info=True)
    else:
        logger.error(exception, exc_info=True)


def log_false_email(text):
    with open(Constant.FALSE_EMAIL_FILE, 'a+') as log:
        date_time = datetime.now()
        print_unrecognized_encoding(f"{date_time}: {text}", file=log)


def print_unrecognized_encoding(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f: () = lambda obj: str(obj).encode(enc, errors='replace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


def configure_logging():
    handler = logging.handlers.RotatingFileHandler(
        filename=Constant.LOG_FILE,
        mode='a+',
        maxBytes=5 * 1024 * 1024,
        backupCount=2,
        encoding='utf-8'
    )
    formatter = logging.Formatter('%(asctime)s|%(levelname)s: %(message)s',
                                  '%d/%m/%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


def setup_logging():
    configure_logging()
