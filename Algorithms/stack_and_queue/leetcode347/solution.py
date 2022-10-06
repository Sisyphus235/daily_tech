# -*- coding: utf8 -*-

import heapq

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    stats = {}
    for i in range(len(nums)):
        stats[nums[i]] = stats.get(nums[i], 0) + 1
    pri_que = []
    for key, freq in stats.items():
        heapq.heappush(pri_que, (-freq, key))
    result = []
    for i in range(k):
        result.append(heapq.heappop(pri_que)[1])
    return result


if __name__ == '__main__':
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
