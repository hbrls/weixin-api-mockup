# -*- coding: utf-8 -*-
from os import environ
from .default import DefaultConfig


class ProductionConfig(DefaultConfig):

    DEBUG = False

    # APP_DOMAIN = environ['APP_DOMAIN']
    # APP_PORT = environ['APP_PORT']

    # # SQLAlchemy connection options
    # SQLALCHEMY_DATABASE_URI = 'mysql://%(user)s:%(pass)s@%(addr)s/%(db)s' % {
    #     'user': environ['APP_MYSQL_USER'],
    #     'pass': environ['APP_MYSQL_PASS'],
    #     'addr': environ['MYSQL_PORT_3306_TCP_ADDR'],
    #     'db': environ['APP_MYSQL_USER'],
    # }
    # SQLALCHEMY_ECHO = False
    # SQLALCHEMY_RECORD_QUERIES = False

    # # ** The deploy script will append the other configs below **

    # Security
    SECRET_KEY = "SECRET_KEY"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "WTF_CSRF_SECRET_KEY"
