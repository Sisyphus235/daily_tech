# -*- coding: utf8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self._head = ListNode()
        self._count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._count:
            return
        self._count += 1
        new_node = ListNode(val)
        pre, cur = None, self._head
        for _ in range(index + 1):
            pre, cur = cur, cur.next
        else:
            pre.next, new_node.next = new_node, cur

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            self._count -= 1
            pre, cur = None, self._head
            for _ in range(index + 1):
                pre, cur = cur, cur.next
            else:
                pre.next, cur.next = cur.next, None


def test_cases():
    obj = MyLinkedList()
    param_1 = obj.get(-1)
    assert param_1 == -1
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    obj.deleteAtIndex(1)


if __name__ == '__main__':
    test_cases()
