#! python
# -*- coding: utf-8 -*-

import os

import logging
from logging.handlers import RotatingFileHandler


class Config(object):
    APP_HOST = 'localhost'
    APP_PORT = 5000
    DEBUG = False
    TESTING = False
    PRODUCTION = False
    SECRET_KEY = 'some_secret_key'
    SSL_DISABLE = True

    """Flask-WTF Configuration"""
    WTF_CSRF_ENABLED = False

    """Flask-SQLAlchemy Configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'  # sql lite
    SQLALCHEMY_BINDS = {}

    """File-Upload Configuration"""
    MAX_CONTENT_LENGTH = 0.5 * 1024 * 1024  # 500 kb
    UPLOAD_FOLDER = '/tmp'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf'])  # file extensions
    IMAGE_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])  # just images

    """LOGGER / LOGGING
    info / debug / warning / error
    e.g.: app.logger.info('this is my log')
    """
    LOG_FILE = os.getenv('FLASK_LOG_FILE') or '/tmp/flaskfactorybone.log'
    LOG_HANDLER = RotatingFileHandler(LOG_FILE, 'a+', 1 * 1024 * 1024, 10)
    LOG_HANDLER.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    LOG_HANDLER.setLevel(logging.INFO)

    """PERFORMANCE SETTINGS"""
    SQLACLHEMY_RECORD_QUERIES = True
    DB_QUERY_TIMEOUT = 0.1

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    PRODUCTION = True
    WTF_CRSF_ENABLED = True
    # DATABASE:
    SQLALCHEMY_DATABASE_URI = 'postgres://dohodathi:password@localhost/flaskbone'


class HerokuConfig(ProductionConfig):
    """ Heroku specific configurations
    if you are using Heroku and/or a heroku hosted database
    heroku config:set FLASK_CONFIG=heroku
    """
    HEROKU_APP = True
    HEROKU_APP_NAME = u'app name'
    HEROKU_PSQL = True
    HEROKU_PSQL_URI = u'postgres://user:password@url:port/database'
    HEROKU_PSQL_NAME = u'heroku envioronment name'
    SQLALCHEMY_DATABASE_URI = HEROKU_PSQL_URI
    LOG_HANDLER = logging.StreamHandler()
    LOG_HANDLER.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    LOG_HANDLER.setLevel(logging.INFO)

    @classmethod
    def init_app(cls, app):
        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    WTF_CRSF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://dohodathi:password@localhost/flaskbone'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CRSF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://dohodathi:password@localhost/flaskbone'


configurations = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'heroku': HerokuConfig,
    'production': ProductionConfig
}
