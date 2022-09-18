# -*- coding: utf8 -*-


def remove_duplicates(s: str) -> str:
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)
    return ''.join(stack)


def remove_duplicates_pointer(s: str) -> str:
    res = list(s)
    slow = fast = 0
    while fast < len(res):
        res[slow] = res[fast]
        if slow > 0 and res[slow] == res[slow - 1]:
            slow -= 1
        else:
            slow += 1
        fast += 1
    return ''.join(res[0: slow])
