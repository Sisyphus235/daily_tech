#!/usr/bin/env bash

echo 'Starting celery'
exec celery -A celery_worker:celery worker -l INFO \
--pidfile=/var/log/celery/%n.pid \
--logfile=/var/log/celery/%n%I.log --detach&

echo 'Starting celery flower'
exec celery -A celery_worker:celery flower --broker=${FLOWER_BROKER} --address=127.0.0.1 --port=5600 --url_prefix=flower&

echo 'Starting gunicorn'
exec gunicorn --worker-class gevent -w 4 -b 0.0.0.0:6000 patched:app
