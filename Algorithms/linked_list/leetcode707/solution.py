# -*- coding: utf8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoubleListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre


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


class MyDoubleLinkedList:
    def __init__(self):
        self._head, self._tail = DoubleListNode(0), DoubleListNode(0)
        self._head.next, self._tail.pre = self._tail, self._head
        self._count = 0

    def _get_node(self, index: int) -> DoubleListNode:
        if index >= self._count // 2:
            node = self._tail
            for _ in range(self._count - index):
                node = node.pre
        else:
            node = self._head
            for _ in range(index + 1):
                node = node.next
        return node

    def _add_node(self, pre: DoubleListNode, next: DoubleListNode, val: int) -> None:
        self._count += 1
        node = DoubleListNode(val)
        pre.next = node
        next.pre = node
        node.pre = pre
        node.next = next

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            return self._get_node(index).val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self._add_node(self._head, self._head.next, val)

    def addAtTail(self, val: int) -> None:
        self._add_node(self._tail.pre, self._tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._add_node(node.pre, node, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            node = self._get_node(index)
            node.pre.next, node.next.pre = node.next, node.pre


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
