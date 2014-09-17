# -*- coding: utf-8 -*-
from flask import Markup
from flask.ext.wtf import Form
from wtforms import (ValidationError, HiddenField, BooleanField, TextField,
                     PasswordField, SubmitField)
from wtforms.validators import Required, Length, Email
from flask.ext.wtf.html5 import EmailField
from appl.vars import PASSWORD_LEN_MIN, PASSWORD_LEN_MAX
from appl.user.models import User, is_email_taken
from appl.extensions import db


class LoginForm(Form):
    next = HiddenField()
    login = TextField(u'邮箱', [Required()])
    password = PasswordField(u'密码', [Required(),
                             Length(PASSWORD_LEN_MIN, PASSWORD_LEN_MAX)])
    remember = BooleanField(u'一周内不用再次登录', default=True)
    submit = SubmitField(u'登录')


class SignupForm(Form):
    next = HiddenField()
    nickname = TextField(u'昵称', [Required()],
                         description=u'朋友们将看到你的名字')
    email = EmailField(u'邮箱', [Required(), Email()],
                       description=u'您在本站的唯一身份标识')
    password = PasswordField(u'密码', [Required(),
                             Length(PASSWORD_LEN_MIN, PASSWORD_LEN_MAX)],
                             description=u'至少 %s 字符' % PASSWORD_LEN_MIN)
    agree = BooleanField(u'我同意 ' +
                         Markup(u'<a target="blank" href="/terms">站点规范</a>'),
                         [Required()],
                         default=True)
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if is_email_taken(field.data):
            raise ValidationError(u'该Email地址已经注册')

    def save(self):
        user = User(self.email.data)
        self.populate_obj(user)

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        return user
