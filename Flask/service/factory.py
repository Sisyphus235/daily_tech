# -*- coding: utf8 -*-

from flask_sqlalchemy import SQLAlchemy

__all__ = ['db']

# database global instance
db = SQLAlchemy()
