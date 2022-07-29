# -*- coding: utf8 -*-

from typing import Union
from linked_list import ListNode


def get_linked_list_length(head: ListNode) -> int:
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


def get_intersect_node(headA: ListNode, headB: ListNode) -> Union[ListNode, None]:
    lenA = get_linked_list_length(headA)
    lenB = get_linked_list_length(headB)
    if lenA >= lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    while headA is not None:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None


def get_intersect_node2(headA: ListNode, headB: ListNode) -> Union[ListNode, None]:
    """
    走的快的一定会追上走的慢的
    一个链表走完就去走另一条列表
    :param headA:
    :param headB:
    :return:
    """
    cur_a, cur_b = headA, headB
    while cur_a != cur_b:
        cur_a = cur_a.next if cur_a else headB
        cur_b = cur_b.next if cur_b else headA
    return cur_a
