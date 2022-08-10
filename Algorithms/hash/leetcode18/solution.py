# -*- coding: utf8 -*-

from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums = sorted(nums)
    result = []
    for first in range(len(nums) - 3):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        for second in range(first + 1, len(nums) - 2):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            third = second + 1
            fourth = len(nums) - 1
            while third < fourth:
                total = nums[first] + nums[second] + nums[third] + nums[fourth]
                if total == target:
                    result.append([nums[first], nums[second], nums[third], nums[fourth]])
                    while third < fourth and nums[third] == nums[third + 1]:
                        third += 1
                    while third < fourth and nums[fourth] == nums[fourth - 1]:
                        fourth -= 1
                    third += 1
                    fourth -= 1
                elif total > target:
                    fourth -= 1
                else:
                    third += 1
    return result


if __name__ == '__main__':
    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
