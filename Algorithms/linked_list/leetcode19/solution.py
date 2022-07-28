# -*- coding: utf8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(next=head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
