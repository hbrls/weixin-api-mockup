# -*- coding: utf-8 -*-
import hashlib
from datetime import datetime
from uuid import uuid1
from sqlalchemy import Column, Integer, SmallInteger, String, ForeignKey, Date
from sqlalchemy.orm import synonym, relationship
from werkzeug import generate_password_hash, check_password_hash
from flask import url_for
from flask.ext.login import UserMixin, current_user
from appl.utils.custom_columns import UTCTimestampType
from appl.utils.db_base import Base
from appl.vars import USER_TITLE_DEFAULT
from appl.extensions import db


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    created = Column(UTCTimestampType, nullable=False)
    updated = Column(UTCTimestampType, nullable=False)
    email = Column(String(63), unique=True, nullable=False)
    active = Column(SmallInteger, nullable=False)
    nickname = Column(String(63), nullable=False)  # 可以是中文
    gravatar = Column(String(127), nullable=False)  # hash
    username = Column(String(63), nullable=False, unique=True)  # 二级域名

    profile = relationship("UserProfile", uselist=False, backref="user")

    # Hide password encryption by exposing password field only.
    _password = Column('password', String(127),  nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = synonym('_password',
                       descriptor=property(_get_password,
                                           _set_password))

    def __init__(self, email, active=True):
        self.created = datetime.utcnow()
        self.updated = datetime.utcnow()
        self.username = uuid1()
        self.email = email
        self.gravatar = hashlib.md5(email).hexdigest()
        self.active = active
        self.profile = UserProfile()

    def __repr__(self):
        return '<created: %s, email: %s> ' % (self.created, self.email)

    @property
    def display_name(self):
        if current_user.id == self.id:
            return u'我'
        else:
            return self.nickname or self.username or self.email

    @property
    def uri(self):
        return url_for('users.index', uid=self.id)

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get(self):
        return self.id

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def authenticate(Klass, login, password):
        u = db.session.query(Klass).filter_by(email=login).first()

        if u:
            authenticated = u.check_password(password)
        else:
            authenticated = False

        return u, authenticated


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    gender = Column(SmallInteger, default=3)
    birthdate = Column(Date)
    location = Column(Integer, default=0)
    title = Column(String(255))  # 140字微博

    def __init__(self):
        self.gender = 3
        self.relationship = 1
        self.title = USER_TITLE_DEFAULT

    def save(self):
        db.session.commit()


def read_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()


def read_user_by_email(email):
    return db.session.query(User).filter_by(email=email).first()


def is_email_taken(email):
    return read_user_by_email(email) is not None
