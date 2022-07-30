# -*- coding: utf8 -*-


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    aplha = {}
    for c in s:
        if c not in aplha:
            aplha[c] = 1
        else:
            aplha[c] += 1
    for c in t:
        if c not in aplha:
            return False
        aplha[c] -= 1
        if aplha[c] < 0:
            return False
    for v in aplha.values():
        if v != 0:
            return False
    return True
