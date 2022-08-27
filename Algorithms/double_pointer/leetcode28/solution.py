# -*- coding: utf8 -*-


def get_next(pattern):
    next = [-1] * len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j > -1 and pattern[j + 1] != pattern[i]:
            j = next[j]
        if pattern[j + 1] == pattern[i]:
            j += 1
        next[i] = j
    return next


def get_str(haystack: str, needle: str):
    """
    在 haystack 中找出 needle 出现的第一个位置
    :param haystack:
    :param needle:
    :return:
    """
    a = len(needle)
    b = len(haystack)
    if a == 0:
        return 0
    next = get_next(needle)
    p = -1
    for j in range(b):
        while p >= 0 and needle[p + 1] != haystack[j]:
            p = next[p]
        if needle[p + 1] == haystack[j]:
            p += 1
        if p == a - 1:
            return j - a + 1
    return -1


if __name__ == '__main__':
    print(get_str('hello', 'll'))
    print(get_str('bbc abcdab abcdabcdabde', 'abcdabd'))
