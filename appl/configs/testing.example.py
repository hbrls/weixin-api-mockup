# -*- coding: utf-8 -*-
from .default import DefaultConfig


class TestingConfig(DefaultConfig):

    # Indicates that it is a testing environment
    DEBUG = True
    TESTING = True

    # SQLAlchemy connection options
    SQLALCHEMY_DATABASE_URI = '_'

    SERVER_NAME = "_"

    # This will print all SQL statements
    SQLALCHEMY_ECHO = False

    # Qiniu
    QINIU_ACCESS_KEY = '_'
    QINIU_SECRET_KEY = '_'
    QINIU_BUCKET = '_'
    QINIU_DOMAIN = '_'

    # Security
    SECRET_KEY = "_"
    WTF_CSRF_ENABLED = False
    WTF_CSRF_SECRET_KEY = "_"
