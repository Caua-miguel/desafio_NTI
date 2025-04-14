import logging
from colorlog import ColoredFormatter

logging_config = dict(
    version = 1,
    formatters = {
        'color': {
            '()': ColoredFormatter,
            'format': '%(log_color)s%(levelname)-8s : %(asctime)s : %(message)s',
            'log_colors': {
                'DEBUG':    'green',
                'INFO':     'cyan',
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
                'filename': 'project/log/var/logs.log',
                'mode': 'a',
                'formatter': 'f',
                'level': logging.WARNING,
                },      
    },
    root = {
        'handlers': ['sh', 'fh'],
        'level': logging.DEBUG,
    },
)