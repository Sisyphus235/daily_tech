# -*- coding: utf8 -*-

from typing import Union

from linked_list import ListNode


def detect_cycle(head: ListNode) -> Union[ListNode, None]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p = head
            q = slow
            while p != q:
                p = p.next
                q = q.next
            return p
    return None