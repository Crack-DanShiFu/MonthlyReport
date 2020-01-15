from flask import request, app, send_from_directory, abort, render_template, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user, login_manager

from page.server import *
from . import page


@page.route('/')
@login_required
def index():
    return render_template('index.html')


@page.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('page.index'))
    form = LoginForm(request.form)
    form.next = request.args.get('next') or ''  # 登录成功后跳转回原来的url
    if request.method == 'POST' and form.validate():
        username = request.form.get('username')
        password = request.form.get('password')
        res = Users.try_ldap_login(username, password)
        if not res:
            current_app.logger.error('ldap login failed')
            return render_template('login.html', form=form)
        else:
            user = Users.query.filter_by(username=username).first()
            if not user:
                user = Users(username, password)
                db.session.add(user)
                db.session.commit()
            login_user(user)
            return redirect(request.args.get('next') or url_for('page.index'))
        if form.errors:
            current_app.logger.error('login form error')
    else:
        return render_template('login.html', form=form)


@page.route('/logout')
@login_required
def logout():
    current_app.logger.debug('log out .....')
    logout_user()
    return redirect(url_for('page.login'))
