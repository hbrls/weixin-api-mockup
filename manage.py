# -*- coding: utf-8 -*-
import subprocess
from flask.ext.script import Manager, Server
from appl import create_app

from appl.configs.development import DevelopmentConfig

app = create_app(DevelopmentConfig)
manager = Manager(app)

# ** The Flask-Script will override app.config['DEBUG']
_USE_DEBUGGER = app.debug

# Run local server
manager.add_command("runserver", Server(host='localhost',
                                        port=5000,
                                        use_debugger=_USE_DEBUGGER))


@manager.command
def init():
    p = subprocess.call(['alembic', 'init', 'alembic'])


@manager.option('-t', '--tag', dest='tag', default='upgrade')
def db_rev(tag):
    p = subprocess.call(['alembic', 'revision', '--autogenerate', '-m', tag])


@manager.option('-r', '--revision', dest='rev', default='head')
def db_upgrade(rev):
    p = subprocess.call(['alembic', 'upgrade', rev])


@manager.option('-r', '--revision', dest='rev', default='head')
@manager.option('-s', '--sql', dest='sql', default='migration.sql')
def db_upgrade_offline(rev, sql):
    p = subprocess.call(['alembic', 'upgrade', rev, '--sql'])


@manager.option('--id', dest='id')
def del_user(id):
    sql = '''
    DELETE FROM user WHERE id = {0};
    '''.format(id)
    print sql


if __name__ == "__main__":
    manager.run()
