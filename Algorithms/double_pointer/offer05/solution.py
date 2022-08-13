# -*- coding: utf8 -*-


def replace_space(s: str) -> str:
    space_count = s.count(' ')
    result = list(s)
    result.extend([' '] * space_count * 2)
    left, right = len(s) - 1, len(result) - 1
    while left >= 0:
        if s[left] != ' ':
            result[right] = result[left]
            right -= 1
        else:
            result[right - 2: right + 1] = '%20'
            right -= 3
        left -= 1
    return ''.join(result)
