
from typing import List


def solution(nums: List[int]) -> List[int]:
    result = [-1 for _ in range(len(nums))]
    current = len(nums) - 1
    left = 0
    right = len(nums) - 1
    while current > -1:
        square_left = nums[left] * nums[left]
        squre_right = nums[right] * nums[right]
        if square_left >= squre_right:
            result[current] = square_left
            left += 1
        else:
            result[current] = squre_right
            right -= 1
        current -= 1
    return result


def test_cases():
    cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ]
    for case in cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
