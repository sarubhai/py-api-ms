import os

basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOSTNAME = os.environ.get('POSTGRES_HOSTNAME')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:5432/{POSTGRES_DB}'
SECRET = os.environ.get('SECRET_KEY')

class BaseConfig:
    """Base Configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SECRET_KEY = SECRET
    SQLALCHEMY_ECHO = True
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SECRET_KEY = SECRET
