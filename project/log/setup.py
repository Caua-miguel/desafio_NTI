import logging.config
import logging
import pathlib
import json
import os

def setup_logging():
    config_file = pathlib.Path(__file__).resolve().parents[2] / 'log_config.json'
    var_folder = pathlib.Path('./project/log/var')
    
    if var_folder.exists() is False:
        os.makedirs(var_folder)

    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)