import logging.config
import logging
import pathlib
import json

def setup_logging():
    config_file = pathlib.Path(__file__).resolve().parents[2] / 'log_config.json'
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)