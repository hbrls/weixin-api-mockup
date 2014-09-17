# -*- coding: utf-8 -*-
from flask.ext.login import current_user
from flask.ext.wtf import Form
from wtforms import (TextField, SubmitField, RadioField,
                     SelectField, PasswordField, ValidationError)
from wtforms.validators import DataRequired, Length
from appl.vars import PASSWORD_LEN_MIN, PASSWORD_LEN_MAX
from appl.dictionary import assemble_choices
from appl.dictionary.gender import GENDERS
from appl.dictionary.location import LOCATIONS
from appl.extensions import db


class UserProfileForm(Form):
    gender = RadioField(u'性别', coerce=int, choices=assemble_choices(GENDERS))
    birthdate = TextField(u'生日', [DataRequired(message=u'请填写生日')])
    location = SelectField(u'所在省市', coerce=int,
                           choices=assemble_choices(LOCATIONS))
    title = TextField(u'简介', [DataRequired(message=u'请填写简介')])
    submit = SubmitField(u'更新')

    def save(self):
        self.populate_obj(current_user.profile)
        db.session.commit()


class UserBasicForm(Form):
    # FIXME: username should be unique
    # username = TextField(u'用户名', [DataRequired()])
    nickname = TextField(u'昵称', [DataRequired()])
    submit = SubmitField(u'更新')

    def save(self):
        self.populate_obj(current_user)
        db.session.commit()


class ResetPasswordForm(Form):
    old_password = PasswordField(u'原密码',
                                 [DataRequired()])
    new_password = PasswordField(u'新密码', [DataRequired(),
                                 Length(PASSWORD_LEN_MIN, PASSWORD_LEN_MAX)],
                                 description=u'至少 %s 字符' % PASSWORD_LEN_MIN)
    repeat_password = PasswordField(u'确认密码', [DataRequired()])
    submit = SubmitField(u'确认修改')

    def validate_old_password(self, field):
        if not current_user.check_password(field.data):
            raise ValidationError(u'原密码输入错误')

    def validate_repeat_password(self, field):
        if field.data != self.new_password.data:
            raise ValidationError(u'两次输入的密码不一致')

    def save(self):
        current_user.password = self.new_password.data
        db.session.commit()
