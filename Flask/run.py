# -*- coding: utf8 -*-

from service.core import create_app
from service.constants import SERVICE_HOST, SERVICE_PORT

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config[SERVICE_HOST],
            port=app.config[SERVICE_PORT],
            debug=False)
