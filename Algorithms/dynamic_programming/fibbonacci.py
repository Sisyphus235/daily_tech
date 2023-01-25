# -*- coding: utf8 -*-

"""
n = 1/2, 1
n > 2, fib(n) = fib(n-1) + fib(n-2)

1.状态
第 n 个数的值

2.dp 数组
第 n 个数的值组成的 array

3.选择方式
dp[i] = dp[i-1] + dp[i-2]

4.base 定义
dp[0] = dp[1] = 1
"""


def fib_dp(n: int) -> int:
    # 边界判断
    if n < 0:
        return -1
    # 初始化 dp table，利用 base case
    dp_table = [0] + [1] * n
    # 状态转移方程逐个求解
    for i in range(2, n + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    # 返回目标值
    return dp_table[n]


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
        print(fib(i), fib_dp(i))
