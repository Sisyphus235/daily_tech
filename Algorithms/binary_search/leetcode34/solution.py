from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    def search_left(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def search_right(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right

    left = search_left(nums, target)
    right = search_right(nums, target)

    return [left, right]


def test_cases():
    test_cases = [([5, 7, 7, 8, 8, 10], 8, [3, 4]), ([5, 7, 7, 8, 8, 10],
                                                     6, [-1, -1]), ([], 0, [-1, -1]), ([1], 1, [0, 0]), ([1], 0, [-1, -1])]
    for case in test_cases:
        assert solution(case[0], case[1]) == case[2]
        assert solution(case[0], case[1]) == case[2]


if __name__ == '__main__':
    test_cases()
