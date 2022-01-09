#!/usr/bin/env bash

echo 'Starting celery'
exec celery -A celery_worker:celery worker -l INFO&

echo 'Starting gunicorn'
exec gunicorn --worker-class gevent -w 4 -b 0.0.0.0:6000 patched:app
