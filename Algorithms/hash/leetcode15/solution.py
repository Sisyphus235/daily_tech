# -*- coding: utf8 -*-

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    难点是不重复，先排序，然后遍历 nums，用双指针在当前值的下一个和最后一个，循环查找不重复的组合
    :param nums:
    :return:
    """
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        # 三数之和，因为正序排列，如果第一个数大于零，不可能找到三数和等于零
        if nums[i] > 0:
            break
        # 如果遍历的第一个数和之前相等，跳过，避免重复
        if i >= 1 and nums[i] == nums[i - 1]:
            continue
        # 二三个数初始值在左右极值位置，之后循环查找
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # 左指针右移，直到值不相等，过滤重复项
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # 右指针左移，直到值不相等，过滤重复项
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1

    return result


if __name__ == '__main__':
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([]) == []
    assert three_sum([0]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
