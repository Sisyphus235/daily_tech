# -*- coding: utf8 -*-

from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    排序后用双指针方式寻找相同的元素，好处是节省内存
    :param nums1:
    :param nums2:
    :return:
    """
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    res = []
    p1 = p2 = 0
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return res
