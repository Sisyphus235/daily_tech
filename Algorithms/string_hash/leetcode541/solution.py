# -*- coding: utf8 -*-


def reverse_str(s: str, k: int) -> str:
    count = 0
    stack = []
    result = []
    for i in range(len(s)):
        count += 1
        if count < k:
            stack.append(s[i])
        elif count == k:
            result.append(s[i])
            while stack:
                result.append(stack.pop(-1))
        elif count < 2 * k:
            result.append(s[i])
        elif count == 2 * k:
            result.append(s[i])
            count = 0
    while stack:
        result.append(stack.pop(-1))
    return ''.join(result)
