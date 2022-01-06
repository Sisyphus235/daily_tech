# -*- coding: utf8 -*-

from gevent import monkey

monkey.patch_all()

from run import app
