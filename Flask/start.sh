#!/usr/bin/env bash

gunicorn --worker-class gevent -w 4 -b 0.0.0.0:6000 patched:app
