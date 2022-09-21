# -*- coding: utf8 -*-

from typing import List


class UdfQueue:
    def __init__(self):
        self.queue = []

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    queue = UdfQueue()
    result = []
    for i in range(k):
        queue.push(nums[i])
    result.append(queue.front())
    for i in range(k, len(nums)):
        queue.pop(nums[i - k])
        queue.push(nums[i])
        result.append(queue.front())
    return result


if __name__ == '__main__':
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
