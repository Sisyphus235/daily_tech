# -*- coding: utf8 -*-

import os
import configparser

from service.constants import SERVICE_CONFIG_MODULE, SERVICE_ENV, SERVICE_DEFAULT_ENV, SERVICE_HOST, SERVICE_PORT, \
    SERVICE_DEFAULT_ENCODING

config_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __getitem__(self, item):
        # 定义按键取值的方法，例如 config[key]
        return getattr(self, item)

    def __setitem__(self, key, value):
        # 定义按键赋值的方法，例如 config[key] = value
        setattr(self, key, value)

    def __new__(cls, *args, **kwargs):
        # 发生在 __init__ 之前，在实例化之前会将参数传递给 __new__ 产生一个实例，然后执行 __init__ 的实例化逻辑
        # 一般用在继承不可变的类之后，改变类实例化的行为；或者用于实现单例
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cf = configparser.RawConfigParser(allow_no_value=True)
        env = os.getenv(SERVICE_ENV, SERVICE_DEFAULT_ENV).lower()
        print(rf'current env is {env}')
        config_path = os.path.join(config_dir, rf'{env}.ini')
        cf.read(config_path, SERVICE_DEFAULT_ENCODING)

        # service
        self[SERVICE_HOST] = cf.get(SERVICE_CONFIG_MODULE, SERVICE_HOST)
        self[SERVICE_PORT] = cf.get(SERVICE_CONFIG_MODULE, SERVICE_PORT)
