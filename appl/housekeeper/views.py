# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required


mod = Blueprint('housekeeper', __name__, template_folder='templates')


@mod.route('/')
@login_required
def index():
    return render_template('housekeepers/index.html')
