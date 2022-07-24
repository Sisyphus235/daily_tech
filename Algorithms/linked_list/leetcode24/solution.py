# -*- coding: utf8 -*-

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: ListNode) -> ListNode:
    dummy = ListNode()
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        cur = pre.next
        post = cur.next

        pre.next = post
        cur.next = post.next
        post.next = cur

        pre = cur
    return dummy.next
