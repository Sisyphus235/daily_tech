from typing import List


def solution(nums: List[int], val: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != val:
            left += 1
        else:
            nums[left] = nums[right]
            right -= 1
    return left


def solution_no_assign(nums: List[int], val: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != val:
            left += 1
            continue
        while nums[right] == val and right > left:
            right -= 1
        if right == left:
            return left
        nums[left] = nums[right]
        right -= 1
        left += 1

    return left


def test_cases():
    cases = [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ([0, 1, 4, 0, 3, 2, 2, 2], 2, 5),
        ([0, 0, 0], 0, 0),
    ]
    for case in cases:
        print(f'assert {case[0], case[1]} == {case[2]}')
        assert solution(case[0], case[1]) == case[2]
        # assert solution_no_assign(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
