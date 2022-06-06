# -*- coding: utf8 -*-

import sys
import logging

from service.constants import SERVICE_LOGGER_NAME


def build_logger():
    # init logger
    logger = logging.getLogger(SERVICE_LOGGER_NAME)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)d]: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S:%MS'
    )
    # init stdout handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    # init stderr handler
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    stderr_filter = logging.Filter()
    stderr_filter.filter = lambda record: record.levelno >= logging.WARNING
    stderr_handler.addFilter(stderr_filter)
    logger.addHandler(stderr_handler)

    return logger


logger = build_logger()
