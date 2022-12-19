# -*- coding: utf8 -*-

"""
n=0, 0
n<0, -1
n>0, min{dp(n-coin) + 1 | coin ∈ coins}
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    memo = {}

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        memo[n] = res if res != float('inf') else -1
        return memo[n]

    return dp(amount)


def coin_change_table(coins: List[int], amount: int) -> int:
    table = [amount + 1 for _ in range(amount + 1)]
    table[0] = 0
    for i in range(len(table)):
        for coin in coins:
            if i - coin < 0:
                continue
            table[i] = min(table[i], 1 + table[i - coin])
    return -1 if table[amount] == amount + 1 else table[amount]


if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    assert coin_change(coins, 27) == 4
    assert coin_change_table(coins, 27) == 4
