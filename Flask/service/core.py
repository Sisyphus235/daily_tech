# -*- coding: utf8 -*-

from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        setup_health(app)

    return app


def setup_health(app):
    @app.route('/health')
    def check_health():
        return 'ok'
