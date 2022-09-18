# -*- coding: utf8 -*-


def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        elif not stack or stack[-1] != c:
            return False
        else:
            stack.pop()
    return not stack


if __name__ == '__main__':
    assert is_valid('[') is False
    assert is_valid('}') is False
    assert is_valid('[}') is False
