import logging
import os
from colorlog import ColoredFormatter

log_file_path = 'project/log/var/logs.log'
log_dir = os.path.dirname(log_file_path)
os.makedirs(log_dir, exist_ok=True)

logging_config = dict(
    version = 1,
    formatters = {
        'color': {
            '()': ColoredFormatter,
            'format': '%(log_color)s%(levelname)-8s : %(asctime)s : %(message)s',
            'log_colors': {
                'DEBUG':    'fg_82',
                'INFO':     'bold_blue',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',
            },
        },
    },
    handlers = {
        'sh': {'class': 'logging.StreamHandler',
                'formatter': 'color',
                'level': logging.DEBUG,
            },
        'fh': {'class': 'logging.FileHandler',
                'filename': log_file_path,
                'mode': 'a',
                'formatter': 'color',
                'level': logging.WARNING,
                },      
    },
    root = {
        'handlers': ['sh', 'fh'],
        'level': logging.DEBUG,
    },
)