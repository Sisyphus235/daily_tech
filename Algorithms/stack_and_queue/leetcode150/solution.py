# -*- coding: utf8 -*-

from typing import List


def eval_RPN(tokens: List[str]) -> int:
    stack = []
    for e in tokens:
        if e not in ('+', '-', '*', '/'):
            stack.append(e)
            continue
        n2 = stack.pop()
        n1 = stack.pop()
        res = int(eval(f'{n1}{e}{n2}'))
        stack.append(res)
    return int(stack[-1])


if __name__ == '__main__':
    assert eval_RPN(["2", "1", "+", "3", "*"]) == 9
    assert eval_RPN(["4", "13", "5", "/", "+"]) == 6
    assert eval_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
