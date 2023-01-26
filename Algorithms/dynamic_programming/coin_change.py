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
    # 初始化
    dp_table = [0] + [-1] * amount
    # 状态转移方程逐个求解，注意边界，dp_table[0] 只是占位略过，dp_table[amount] 是终点
    for i in range(1, amount + 1):
        # 如果当前面额在面额列表中，数量设为 1
        if i in coins:
            dp_table[i] = 1
            continue
        for coin in coins:
            if i - coin <= 0:
                continue
            # 之前面额无解放弃
            if dp_table[i - coin] == -1:
                continue
            dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1) if dp_table[i] != -1 else dp_table[i - coin] + 1
    return dp_table[amount]


if __name__ == '__main__':
    coin_change_table([1], 0)
    coins = [1, 2, 5, 10]
    assert coin_change(coins, 27) == 4
    assert coin_change_table(coins, 27) == 4
