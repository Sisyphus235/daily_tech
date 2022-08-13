# -*- coding: utf8 -*-


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    pre, cur = None, head
    while cur is not None:
        temp = cur.next
        cur.next = pre
        pre, cur = cur, temp

    return pre