
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


def solution_double_pointer(s: str, t: str) -> str:
    result = ''
    t_dict = dict()  # 储存所有字母的数量，先遍历 t 所有的字母遇见 +1，再遍历 s，右指针遇见的字母都 -1
    for c in t:
        if c not in t_dict:
            t_dict[c] = 1
        else:
            t_dict[c] += 1
    left, right, cnt, min_length = 0, 0, 0, len(s) + 1
    while right < len(s):
        if s[right] not in t_dict:
            t_dict[s[right]] = -1
        else:
            t_dict[s[right]] -= 1
        if t_dict[s[right]] >= 0:
            cnt += 1
        # 目标字符串长度和 t 相等时，判断当前符合目标的字符串，如果比记录值小则更新，左指针遍历，遇见的字母都 +1，直到 cnt 有变化
        while cnt == len(t):
            if min_length > right - left + 1:
                min_length = right - left + 1
                result = s[left: left + min_length]
            t_dict[s[left]] += 1
            if t_dict[s[left]] > 0:
                cnt -= 1
            left += 1
        right += 1
    return result


def test_cases():
    cases = [
        ("ADOBECODEBANC",  "ABC", "BANC"),
        ("a",  "a", "a"),
        ("a",  "aa", ""),
    ]
    for case in cases:
        print(f'assert {case[0]}, {case[1]} == {case[2]}')
        # assert solution(case[0], case[1]) == case[2]
        assert solution_double_pointer(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
