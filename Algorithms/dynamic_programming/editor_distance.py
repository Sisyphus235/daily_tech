# -*- coding: utf8 -*-

"""
给定两个字符串 s1 和 s2，计算出将 s1 转换为 s2 所使用的最少操作数。
允许的操作包括：插入、删除、替换

例1：s1 = 'horse', s2 = 'ros'
horse -> rorse -> rose -> ros，答案是 3

例2：s1 = 'intention', s2 = 'execution'
intention -> inention -> enention -> exention -> exection -> execution，答案是 5

1.状态
s1 和 s2 在位置 i,j 上的最小编辑距离

2.dp 数组
dp[i,j] 表示 s1[0..i] 和 s2[0..j] 的最小编辑距离

3.选择方式
s1[i] = s2[j] 跳过，dp[i][j] = dp[i-1][j-1]
s1[i] != s2[j] 替换，dp[i][j] = dp[i-1][j-1] + 1
               删除，dp[i][j] = dp[i-1][j] + 1
               插入，dp[i][j] = dp[i][j-1] + 1
               选择 min(替换，删除，插入)

dp[i-1][j-1],    dp[i-1][j]
     替换/跳过 ↘     ↓ 删除
dp[i][j-1],插入→  dp[i][j]

s1\s2 "", a, p, p, l, e
""     0, 1, 2, 3, 4, 5
r      1, 1, 2, 3, 4, 5
a      2, 1, 2, 3, 4, 5
d      3, 2, 2, 3, 4, 5

4.base 定义
dp[..][0] 表示 s1 转换为空字符串需要的最少操作数，每个值都和 s1 长度相同，相当于每次都是删除；
dp[0][..] 表示空字符串转换为 s2 需要的最少操作数，每个值都和 s2 长度相同，相当于每次都是插入。

s1\s2 "", a, p, p, l, e
""     0, 1, 2, 3, 4, 5
r      1
a      2
d      3
"""


def print_dp_table(dp_table):
    for i in range(len(dp_table)):
        for j in range(len(dp_table[i])):
            print(dp_table[i][j], end=', ')
        print()
    print()


def editor_distance(s1: str, s2: str) -> int:
    # init dp table
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp_table = [[0 for j in range(len_s2 + 1)] for i in range(len_s1 + 1)]
    print_dp_table(dp_table)
    # base condition
    for i in range(len_s1 + 1):
        dp_table[i][0] = i
    for j in range(len_s2 + 1):
        dp_table[0][j] = j
    print_dp_table(dp_table)
    # dp table calc
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1]
            else:
                dp_table[i][j] = min(dp_table[i - 1][j - 1] + 1, dp_table[i - 1][j] + 1, dp_table[i][j - 1] + 1)
    print_dp_table(dp_table)
    # return target
    return dp_table[len_s1][len_s2]


if __name__ == '__main__':
    assert editor_distance('rad', 'apple') == 5
    assert editor_distance('horse', 'ros') == 3
    assert editor_distance('intention', 'execution') == 5
