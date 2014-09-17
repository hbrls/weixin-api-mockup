# -*- coding: utf-8 -*-
from datetime import timedelta


class DefaultConfig(object):

    DEBUG = False
    TESTING = False

    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = False

    # Flask-Login
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
