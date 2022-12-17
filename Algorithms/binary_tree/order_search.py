# -*- coding: utf8 -*-

"""
binary tree
    1
  /   \
  2   3
/  \  / \
4  5  6
"""

from typing import List, Union


class Node:
    def __init__(self, val: Union[int, None] = None):
        self.val = val
        self.left = None
        self.right = None


def binary_tree_search(root: Node) -> List[int]:
    result = []
    queue = []
    if root is None:
        return result
    else:
        queue.append(root)
    while queue:
        node = queue.pop()
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
        result.append(node.val)
    return result


if __name__ == '__main__':
    assert binary_tree_search(None) == []

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6

    assert binary_tree_search(n1) == [1, 2, 3, 4, 5, 6]
