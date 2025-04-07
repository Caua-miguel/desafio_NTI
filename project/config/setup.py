import os
from dotenv import load_dotenv

load_dotenv(override=True)

def setup():
    mode=os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from project.config.settings import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from project.config.settings import TestingConfig
            return TestingConfig
        elif mode == 'DEVELOPMENT':
            from project.config.settings import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from project.config.settings import AplicationConfig
        return AplicationConfig