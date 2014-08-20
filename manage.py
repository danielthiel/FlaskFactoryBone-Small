#! python
# -*- coding: utf-8 -*-

import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


""" enable migration / alembic for sqlalchemy:
    first time using it:
        python manage.py db init
        # all generated files must be added to version control !
    how to create automati migration script:
        python manage.py db migrate -m "message"
    deploy the migration:
        python manage.py db upgrade
"""
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def db_reset():
    app.logger.info('drop and create database: {0}'.
        format(app.config.get('SQLALCHEMY_DATABASE_URI')))
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()
