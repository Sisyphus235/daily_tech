# -*- coding: utf8 -*-


def can_construct(ransom_note: str, magazine: str) -> bool:
    if len(ransom_note) > len(magazine):
        return False
    alpha = {}
    for c in magazine:
        if c in alpha:
            alpha[c] += 1
        else:
            alpha[c] = 1
    for c in ransom_note:
        if c not in alpha:
            return False
        alpha[c] -= 1
        if alpha[c] < 0:
            return False
    return True
