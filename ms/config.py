import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

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

class TestingConfig(BaseConfig):
    """Testing Configuration"""
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'test.db')}"
    SECRET_KEY = SECRET
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production Configuration"""
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SECRET_KEY = SECRET
