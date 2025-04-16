from project.log.config import logging_config
import os
import logging

def env_filter():
    
    mode=os.environ.get('MODE')

    if mode == 'PRODUCTION':
        log_dict = logging_config
        log_dict['handlers']['sh']['level'] = logging.INFO
        return log_dict
    elif mode == 'DEVELOPMENT':
        log_dict = logging_config
        log_dict['handlers']['sh']['level'] = logging.DEBUG
        return log_dict