# -*- coding: utf8 -*-

from flask import Flask

from config import app_config
from service.factory import db


def create_app():
    app = Flask(__name__)

    with app.app_context():
        setup_config(app)
        setup_db(app)
        setup_health(app)

    return app


def setup_config(app):
    app.config.from_object(app_config)


def setup_db(app):
    db.app = app
    db.init_app(app)


def setup_health(app):
    @app.route('/health')
    def check_health():
        return 'ok'
