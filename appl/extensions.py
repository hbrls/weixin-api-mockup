# -*- coding: utf-8 -*-
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

login_manager = LoginManager()
