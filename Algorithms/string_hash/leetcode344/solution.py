# -*- coding: utf8 -*-

from typing import List


def reverse_string(s: List[str]) -> None:
    head, end = 0, len(s) - 1
    while head < end:
        temp = s[head]
        s[head] = s[end]
        s[end] = temp
        head += 1
        end -= 1
