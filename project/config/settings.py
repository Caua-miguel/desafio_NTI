import os

class AplicationConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r'sqlite:///:memory:'

class ProductionConfig(AplicationConfig):
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"

class DevelopmentConfig(AplicationConfig):
    DEBUG = True

class TestingConfig(AplicationConfig):
    TESTING = True