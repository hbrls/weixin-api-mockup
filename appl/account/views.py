# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, flash
from flask.ext.login import current_user, login_required
from .forms import UserProfileForm, UserBasicForm, ResetPasswordForm


mod = Blueprint('accounts', __name__, template_folder='templates')


@mod.route('/basic', methods=['GET', 'POST'])
@login_required
def basic():
    form = UserBasicForm(obj=current_user)

    if form.validate_on_submit():
        form.save()
        flash(u'注册资料更新成功', 'success')

    return render_template('accounts/basic.html', form=form)


@mod.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserProfileForm(obj=current_user.profile)

    if form.validate_on_submit():
        form.save()
        flash(u'个人介绍更新成功', 'success')

    return render_template('accounts/profile.html', form=form)


@mod.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        form.save()
        flash(u'您的密码已经更新', 'success')

    return render_template('accounts/reset_password.html', form=form)
