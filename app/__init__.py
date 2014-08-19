#! python
# -*- coding: utf-8 -*-

from flask import Flask

# initialise the database:
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import get_debug_queries
db = SQLAlchemy()


def create_app(config):
    """create flaks app object"""

    # Initialize the App:
    app = Flask(__name__)
    from config import configurations
    app.config.from_object(configurations[config])
    configurations[config].init_app(app)
    app.logger.addHandler(app.config.get('LOG_HANDLER'))
    app.logger.info('App is starting!')

    db.init_app(app)

    # Register the Main Views:
    from .views import api
    app.register_blueprint(api, url_prefix='/api/v1')

    @app.after_request
    def after_request(resp):
        for q in get_debug_queries():
            if q.duration > app.config.get('DB_QUERY_TIMEOUT'):
                app.logger.warning(
                    'SLOW DB STATEMENT: {0}\n\tParameters: {1}\n\tDuration: {2}\n\tContext: {3}'.
                    format(q.statement, q.parameters, q.duration, q.context))
        return resp

    return app
