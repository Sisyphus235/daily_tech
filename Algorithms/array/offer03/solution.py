# -*- coding: utf8 -*-

def find_repeat_number(nums: [int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]: return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


if __name__ == '__main__':
    assert find_repeat_number([2, 3, 1, 0, 2, 5, 3]) == 2
    assert find_repeat_number([3, 4, 2, 1, 1, 0]) == 1
