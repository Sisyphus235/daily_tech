# -*- coding: utf8 -*-

from typing import NamedTuple


class BaseUserDTO(NamedTuple):
    name: str
    phone: str
    email: str


class UserDTO(BaseUserDTO):
    def __new__(cls, name: str = '', phone: str = '', email: str = ''):
        return super(BaseUserDTO, cls).__new__(cls, (name, phone, email))
