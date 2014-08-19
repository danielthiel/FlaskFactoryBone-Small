#! python
# -*- coding: utf-8 -*-

import os

from flask.ext.script import Manager
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@manager.command
def db_reset():
    app.logger.info('drop and create database: {0}'.
        format(app.config.get('SQLALCHEMY_DATABASE_URI')))
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()
