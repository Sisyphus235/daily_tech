# -*- coding: utf8 -*-

from typing import List


def four_sum_count(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    record = {}
    for n1 in nums1:
        for n2 in nums2:
            total = n1 + n2
            if total in record:
                record[total] += 1
            else:
                record[total] = 1
    count = 0
    for n3 in nums3:
        for n4 in nums4:
            target = - n3 - n4
            if target in record:
                count += record[target]
    return count


if __name__ == '__main__':
    count = four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])
    assert count == 2
