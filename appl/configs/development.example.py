# -*- coding: utf-8 -*-
from .default import DefaultConfig


class DevelopmentConfig(DefaultConfig):

    DEBUG = True

    APP_DOMAIN = 'http://127.0.0.1'
    APP_PORT = '5000'

    # SQLAlchemy connection options
    SQLALCHEMY_DATABASE_URI = 'mysql://_:_@localhost/_'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = False

    # Qiniu
    QINIU_ACCESS_KEY = '_'
    QINIU_SECRET_KEY = '_'
    QINIU_BUCKET = '_'
    QINIU_DOMAIN = '_'

    # SendGrid
    SENDGRID_USERNAME = '_'
    SENDGRID_PASSWORD = '_'

    # logging
    LOGENTRIES_TOKEN = '_'

    # Security
    SECRET_KEY = "_"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "_"
