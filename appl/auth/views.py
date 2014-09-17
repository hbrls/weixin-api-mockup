# -*- coding: utf-8 -*-
from flask import (Blueprint, request, render_template, flash, redirect,
                   url_for)
from flask.ext.login import (
    current_user, login_user, logout_user, login_required)
from .forms import LoginForm, SignupForm
from appl.user.models import User


mod = Blueprint('auth', __name__, template_folder='templates')


@mod.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('home.index', uid=current_user.id))

    login_form = LoginForm(login=request.args.get('login', None),
                           next=request.args.get('next', None))

    if login_form.validate_on_submit():
        user, authenticated = User.authenticate(login_form.login.data,
                                                login_form.password.data)

        if user and authenticated:
            login_user(user, remember=login_form.remember.data)
            return redirect(login_form.next.data or
                            url_for('home.index', uid=current_user.id))
        else:
            flash(u'登录邮箱或密码错误', 'error')

    return render_template('auth/login.html', login_form=login_form)


@mod.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated():
        return redirect(url_for('home.index', uid=current_user.id))

    signup_form = SignupForm(next=request.args.get('next'))

    if signup_form.validate_on_submit():
        u = signup_form.save()

        if login_user(u):
            return redirect(signup_form.next.data or
                            url_for('home.index', uid=current_user.id))

    return render_template('auth/signup.html', signup_form=signup_form)


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@mod.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return redirect(url_for('home.not_ready'))
