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
