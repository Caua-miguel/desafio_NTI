import logging
import os

class EnvStreamHandler(logging.StreamHandler):

    def __init__(self, stream: str | None=None):
        super().__init__(stream)
        
        mode=os.environ.get('MODE')

        if mode == 'PRODUCTION':
            self.setLevel(logging.INFO)
        else:
            self.setLevel(logging.DEBUG)