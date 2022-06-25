
from typing import List


def solution(target: int, nums: List[int]) -> int:
    left = right = result = total = 0
    while True:
        if total < target and right < len(nums):
            total += nums[right]
            right += 1
        elif total >= target and left < len(nums):
            result = result if result and right - left > result else right - left
            total -= nums[left]
            left += 1
        else:
            break

    return result


def test_cases():
    cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (7, [1, 1, 1, 1, 5, 1, 1, 4], 3),
        (3, [1, 4, 1], 1)
    ]
    for case in cases:
        print(f'assert {case[0]}, {case[1]} == {case[2]}')
        assert solution(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
