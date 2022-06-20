from typing import List


def solution(nums: List[int]) -> None:
    """
    slow 非零则都前进，slow 为零则 fast 找一个非 0 的交换
    """
    if not nums:
        return
    slow = fast = 0
    while fast < len(nums) - 1:
        if nums[slow] != 0:
            slow += 1
            fast += 1
        else:
            fast += 1
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


def solution_clean(nums: List[int]) -> None:
    """
    fast 遍历一遍，所有非零写到 slow，最后 slow 开始到结尾都写 0
    """
    slow = fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    for i in range(slow, len(nums)):
        nums[i] = 0


def solution_cleaner(nums: List[int]) -> None:
    """
    slow 左侧都是非零的，fast 到 slow 之间都是零
    """
    slow = fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1


def test_cases():
    cases = [
        # ([], []),
        # ([1, 2, 3, 0, 4, 0, 3], [1, 2, 3, 4, 3, 0, 0])
        # ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        # ([0], [0]),
        ([0, 1, 2], [1, 2, 0]),
    ]
    for case in cases:
        print(f'assert {case[0]} == {case[1]}')
        solution(case[0])
        assert case[0] == case[1]


if __name__ == '__main__':
    test_cases()
