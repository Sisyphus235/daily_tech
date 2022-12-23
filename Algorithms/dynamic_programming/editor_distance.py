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

from enum import IntEnum


class ChoiceEnum(IntEnum):
    INIT = 0
    INSERT = 1
    DELETE = 2
    REPLACE = 3
    SKIP = 4


class EditorNode:
    def __init__(self, val: int, choice: ChoiceEnum = ChoiceEnum.INIT):
        self.val = val
        self.choice = choice


def print_dp_table(dp_table):
    for i in range(len(dp_table)):
        for j in range(len(dp_table[i])):
            if isinstance(dp_table[i][j], EditorNode):
                print(f'{dp_table[i][j].val}({dp_table[i][j].choice.name:8})', end=', ')
            else:
                print(dp_table[i][j], end=', ')
        print()
    print()


def print_choice(dp_table, s1: str, s2: str):
    i, j = len(s1), len(s2)
    choice_list = []
    while i > 0 or j > 0:
        choice = dp_table[i][j].choice
        if choice == ChoiceEnum.REPLACE:
            choice_list.insert(0, f'{choice.name} {s1[i - 1]} with {s2[j - 1]}')
            i -= 1
            j -= 1
        elif choice == ChoiceEnum.SKIP:
            choice_list.insert(0, f'{choice.name} same alphabet {s1[i - 1]}')
            i -= 1
            j -= 1
        elif choice == ChoiceEnum.INSERT:
            choice_list.insert(0, f'{choice.name} {s2[j - 1]}')
            j -= 1
        else:
            choice_list.insert(0, f'{choice.name} {s1[i - 1]}')
            i -= 1
    print(f'{s1} to {s2}: {" => ".join(choice_list)}')


def editor_distance(s1: str, s2: str) -> int:
    # init dp table
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp_table = [[0 for j in range(len_s2 + 1)] for i in range(len_s1 + 1)]
    print_dp_table(dp_table)
    # base condition
    for i in range(1, len_s1 + 1):
        dp_table[i][0] = i
    for j in range(1, len_s2 + 1):
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


def editor_distance_choice(s1: str, s2: str) -> int:
    # init dp table
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp_table = [[EditorNode(0) for j in range(len_s2 + 1)] for i in range(len_s1 + 1)]
    print_dp_table(dp_table)
    # base condition
    for i in range(1, len_s1 + 1):
        dp_table[i][0] = EditorNode(i, ChoiceEnum.DELETE)
    for j in range(1, len_s2 + 1):
        dp_table[0][j] = EditorNode(j, ChoiceEnum.INSERT)
    print_dp_table(dp_table)
    # dp table calc
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp_table[i][j] = EditorNode(dp_table[i - 1][j - 1].val, ChoiceEnum.SKIP)
            else:
                min_val = min(dp_table[i - 1][j - 1].val, dp_table[i - 1][j].val, dp_table[i][j - 1].val)
                if min_val == dp_table[i - 1][j - 1].val:
                    dp_table[i][j] = EditorNode(min_val + 1, ChoiceEnum.REPLACE)
                elif min_val == dp_table[i - 1][j].val:
                    dp_table[i][j] = EditorNode(min_val + 1, ChoiceEnum.DELETE)
                else:
                    dp_table[i][j] = EditorNode(min_val + 1, ChoiceEnum.INSERT)
    print_dp_table(dp_table)
    print_choice(dp_table, s1, s2)
    return dp_table[len_s1][len_s2].val


if __name__ == '__main__':
    assert editor_distance('rad', 'apple') == 5
    assert editor_distance_choice('rad', 'apple') == 5

    assert editor_distance('horse', 'ros') == 3
    assert editor_distance_choice('horse', 'ros') == 3

    assert editor_distance('intention', 'execution') == 5
    assert editor_distance_choice('intention', 'execution') == 5
