# -*- coding: utf8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode, val: int) -> ListNode:
    dummy = ListNode()
    dummy.next = head
    cur = dummy
    while cur.next is not None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


def test_cases():
    test_cases = [
        # ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, [])
    ]
    for case in test_cases:
        print(f'assert {case[0]} remove {case[1]} == {case[2]}')
        if not case[0]:
            head = ListNode()
        else:
            dummy = ListNode()
            cur = dummy
            for e in case[0]:
                cur.next = ListNode(e)
                cur = cur.next
            head = dummy.next
        result = solution(head, case[1])
        result_to_list = []
        while result is not None and result.val != 0:
            result_to_list.append(result.val)
            result = result.next
        assert result_to_list == case[2]


if __name__ == '__main__':
    test_cases()
