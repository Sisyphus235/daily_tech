
from typing import Dict, Tuple


def solution(s: str, t: str) -> str:
    def _get_last_character(t_index_dict: Dict, target: str) -> Tuple[str, int]:
        result = None
        last_position = None
        for (s, i), position in t_index_dict.items():
            if s != target:
                continue
            if position is None:
                return (s, i)
            if result is None:
                result, last_position = (s, i), position
            else:
                if position < last_position:
                    result, last_position = (s, i), position
        return result

    def _get_substring(t_index_dict: Dict, s: str) -> str:
        if any(x is None for x in t_index_dict.values()):
            return ''
        left = right = None
        for pos in t_index_dict.values():
            if left is None or right is None:
                left = right = pos
            if pos < left:
                left = pos
            if pos > right:
                right = pos
        return s[left: right + 1]

    result = ''
    t_index_dict = {(c, i): None for i, c in enumerate(t)}
    for i, c in enumerate(s):
        if c not in t:
            continue
        last_character = _get_last_character(t_index_dict, c)
        t_index_dict[last_character] = i
        substring = _get_substring(t_index_dict, s)
        if substring:
            if not result:
                result = substring
            elif len(substring) < len(result):
                result = substring

    return result


def test_cases():
    cases = [
        ("ADOBECODEBANC",  "ABC", "BANC"),
        ("a",  "a", "a"),
        ("a",  "aa", ""),
    ]
    for case in cases:
        print(f'assert {case[0]}, {case[1]} == {case[2]}')
        assert solution(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
