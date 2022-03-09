# -*- coding: utf8 -*-

from service.dtos import UserDTO


def test_user_dto_full():
    user_dto = UserDTO(name='tom', phone='15823453421', email='tom@gmail.com')
    assert user_dto.name == 'tom'
    assert user_dto.phone == '15823453421'
    assert user_dto.email == 'tom@gmail.com'
