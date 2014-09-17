# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required


mod = Blueprint('home', __name__, template_folder='templates')


@mod.route('/')
@login_required
def index():
    return render_template('home/index.html')


@mod.route('/not_ready')
def not_ready():
    return render_template('errors/not_ready.html')
