from typing import List


def solution(nums: List[int]) -> int:
    if not nums:
        return 0
    left = 0
    for i in range(len(nums)):
        if left is None:
            left = i
            continue
        if nums[i] == nums[left]:
            continue
        left += 1
        nums[left] = nums[i]
    return left + 1


def test_cases():
    cases = [
        ([], 0),
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([0, 1, 2], 3),
    ]
    for case in cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
