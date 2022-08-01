# -*- coding: utf8 -*-

from typing import List, Union


def two_sum(nums: List[int], target: int) -> Union[List[int], None]:
    record = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in record:
            return [i, record[res]]
        else:
            record[nums[i]] = i
    return None
