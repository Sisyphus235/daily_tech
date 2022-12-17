# -*- coding: utf8 -*-

"""
n = 1/2, 1
n > 2, fib(n) = fib(n-1) + fib(n-2)
"""


def fib(n) -> int:
    if n < 1:
        raise RuntimeError('Invalid n')
    if n in (1, 2):
        return 1
    pre = cur = 1
    target = 2
    while target < n:
        temp = cur
        cur = pre + cur
        pre = temp
        target += 1
    return cur


if __name__ == '__main__':
    for i in range(1, 100):
        print(fib(i))
