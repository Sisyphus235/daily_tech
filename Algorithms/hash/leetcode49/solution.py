# -*- coding: utf8 -*-

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    cases = {}
    for case in strs:
        key = ''.join(sorted(case))
        if key in cases:
            cases[key].append(case)
        else:
            cases[key] = [case]
    result = []
    for value in cases.values():
        result.append(value)
    return result
