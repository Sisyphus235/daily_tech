# -*- coding: utf8 -*-

from typing import List


def find_anagrams(s: str, p: str) -> List[int]:
    aplha = {}
    for c in p:
        if c not in aplha:
            aplha[c] = 1
        else:
            aplha[c] += 1
    result = []
    for i in range(len(s) - len(p) + 1):
        check = aplha.copy()
        for c in s[i: i + len(p)]:
            if c not in check:
                break
            check[c] -= 1
            if check[c] < 0:
                break
        else:
            result.append(i)
    return result


def find_anagrams_slide(s: str, p: str) -> List[int]:
    """
    滑动双指针方式提高效率，但是只能限制在有限集合字母的范畴，否则不在 p 内的字母用 hash 不好处理
    :param s:
    :param p:
    :return:
    """
    result = []
    cnts = [0] * 26
    for c in p:
        cnts[ord(c) - ord('a')] += 1
    left, right = 0, 0
    while right < len(s):
        cnts[ord(s[right]) - ord('a')] -= 1
        while left <= right and cnts[ord(s[right]) - ord('a')] < 0:
            cnts[ord(s[left]) - ord('a')] += 1
            left += 1
        if right - left + 1 == len(p):
            result.append(left)
        right += 1

    return result


if __name__ == '__main__':
    assert find_anagrams('abab', 'ab') == [0, 1, 2]
    assert find_anagrams_slide('abab', 'ab') == [0, 1, 2]
