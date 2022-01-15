# -*- coding: utf8 -*-

import sys
import logging

from service.constants import SERVICE_LOGGER_NAME


def build_logger():
    # init logger
    logger = logging.getLogger(SERVICE_LOGGER_NAME)
    logger.setLevel(logging.INFO)
    # init stdout handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)d]: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S:%MS'
    )
    stdout_handler.setFormatter(stdout_formatter)
    logger.addHandler(stdout_handler)
    # init stderr handler
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s [%(filename)s:%(lineno)d] [process:%(process)d] [thread:%(thread)d]: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S:%MS'
    )
    stderr_handler.setFormatter(stderr_formatter)
    logger.addHandler(stderr_handler)

    return logger


logger = build_logger()
