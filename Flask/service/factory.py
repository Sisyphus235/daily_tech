# -*- coding: utf8 -*-

from flask_sqlalchemy import SQLAlchemy

from service.factories import CeleryFactory

__all__ = ['db', 'celery']

# database global instance
db = SQLAlchemy()

# celery global instance
celery = CeleryFactory()
