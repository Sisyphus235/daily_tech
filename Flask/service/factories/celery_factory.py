# -*- coding: utf8 -*-

from celery import Celery


class CeleryFactory(Celery):
    def __init__(self, app=None):
        super().__init__()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        super().__init__(app.import_name,
                         broker=app.config['CELERY_BROKER'],
                         backend=app.config['CELERY_BACKEND'])
