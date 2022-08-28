# -*- coding: utf8 -*-


def get_next(pattern: str) -> list:
    next_list = [-1] * len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j > -1 and pattern[i] != pattern[j + 1]:
            j = next_list[j]
        if pattern[i] == pattern[j + 1]:
            j += 1
        next_list[i] = j
    return next_list


def repeated_substring_pattern(s: str) -> bool:
    if len(s) == 0:
        return False
    next_list = get_next(s)
    if next_list[-1] != -1 and len(s) % (len(s) - (next_list[-1] + 1)) == 0:
        return True
    return False


if __name__ == '__main__':
    assert repeated_substring_pattern('abab') is True
    assert repeated_substring_pattern('aba') is False
    assert repeated_substring_pattern('abcabcabcabc') is True
