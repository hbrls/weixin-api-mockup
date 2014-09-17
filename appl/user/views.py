# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from flask.ext.login import login_required
from appl.user.models import read_user


mod = Blueprint('users', __name__, template_folder='templates')


@mod.url_value_preprocessor
@login_required
def inject_wg_user(endpoint, values):
    if 'uid' in values:
        g.wg_user = read_user(values['uid'])
    else:
        raise ValueError('uid is missing')


@mod.route('/<int:uid>')
@login_required
def index(uid):
    return render_template('users/index.html')
