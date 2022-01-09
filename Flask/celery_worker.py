# -*- coding: utf8 -*-

from service.core import create_app
from service.factory import celery

celery_app = create_app()
celery_app.app_context().push()
