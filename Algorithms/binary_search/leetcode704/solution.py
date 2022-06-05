from typing import List


def solution_close(nums: List[int], target: int) -> int:
    """
    闭区间解法，[left,right]
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (right + left) // 2
        if target == nums[middle]:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def solution_open(nums: List[int], target: int) -> int:
    """
    开区间解法，[left, right)]
    """
    left = 0
    right = len(nums)
    while left < right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif nums[middle] > target:
            right = middle
        else:
            left = middle + 1
    return -1


def test_cases():
    test_cases = [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12],
                                                 2, -1), ([], 2, -1), ([1], 1, 0), ([1], 0, -1)]
    for case in test_cases:
        assert solution_close(case[0], case[1]) == case[2]
        assert solution_open(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
