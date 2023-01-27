# -*- coding: utf8 -*-

"""
一个无序整数数组，求最长递增子序列的长度
输入 [10,9,2,5,3,7,101,18]
输出 4
最长递增子序列是 [2,3,7,101]
注意区分子序列和子串，子序列不要求连续，子串必须连续

1.状态
[10,9,2,5,3,7,101,18] 中的每个 index，定义状态是这个 index 对应值的最长子序列长度
例如，
10 对应的状态是 1（10）
9 对应的状态是 1（9）
5 对应的状态是 2（2,5）
7 对应的状态是 3（2,3,7）

2.dp 数组含义
dp[i] 表示 index 是 i 的无序整数数组的状态值
例如，[10,9,2,5,3,7,101,18] 对应的 dp 数组是 [1,1,1,2,2,3,4,4]

3."选择"方式
dp[i] 基于 dp[0~i-1] 来计算，先获得 target=array[i]，循环 index j 0~i-1，如果 array[j] < target，则当前状态可以是 dp[j]+1，
循环获得其中状态的最大值就是 dp[i] 的值

4.base 定义
任何一个 index 的值都可以是当前值本身的子序列长度，所以 base 值是 1，dp 数组是长短为 array 长短且所有值为 1 的数组
"""

from typing import List


def get_longest_increasing_subsequence(array: List[int]) -> int:
    dp_table = [1 for _ in range(len(array))]
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i]:
                dp_table[i] = max(dp_table[j] + 1, dp_table[i])
    return max(dp_table)


def longest_increasing_subsequence(nums: List[int]) -> int:
    # 初始化
    dp_table = [1] * len(nums)
    # 状态转移方程逐个求解，index=0 可越过
    for i in range(1, len(nums)):
        # 寻找第一个小于当前整数值的位置
        j = i - 1
        while j >= 0:
            if nums[j] < nums[i]:
                dp_table[i] = max(dp_table[i], dp_table[j] + 1)
            j -= 1
    return max(dp_table)


if __name__ == '__main__':
    # assert get_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    # assert get_longest_increasing_subsequence([1, 4, 3, 4, 2]) == 3
    longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
