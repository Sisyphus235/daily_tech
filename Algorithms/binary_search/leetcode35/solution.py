from typing import List


def solution(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if target == nums[middle]:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return left


def test_cases():
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 4, 2)
    ]
    for case in cases:
        print(
            f'assert {case[0]}, {case[1]} == {case[2]}, actual value {solution(case[0], case[1])}')
        assert solution(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
