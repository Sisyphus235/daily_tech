# -*- coding: utf8 -*-

from service.logger import logger
from service.constants import SERVICE_LOGGER_NAME


def test_logger():
    extra = dict(request_id='MOCK_REQUEST_ID')
    assert logger.name == SERVICE_LOGGER_NAME
    assert len(logger.handlers) == 2
    logger.debug('debug test', extra=extra)
    logger.info('info test', extra=extra)
    logger.warning('warning test', extra=extra)
    try:
        a = 1 / 0
    except ZeroDivisionError:
        logger.error("error test", exc_info=True, extra=extra)
        logger.critical("critical test", exc_info=True, extra=extra)
        logger.error('', exc_info=True, extra=extra)