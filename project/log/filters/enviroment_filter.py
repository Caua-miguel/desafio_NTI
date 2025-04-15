from logging import DEBUG, INFO, NOTSET
import logging
import os

def env_filter():
    mode=os.environ.get('MODE')

    logger = logging.getLogger()
    logger.setLevel(NOTSET)

    for handler in logger.handlers:
        if mode == 'PRODUCTION':
            handler.setLevel(INFO)
            return {}
        elif mode == 'DEVELOPMENT':
            handler.setLevel(DEBUG)
            return {}