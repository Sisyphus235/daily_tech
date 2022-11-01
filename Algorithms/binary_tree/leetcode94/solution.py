# -*- coding: utf8 -*-

from typing import List
from binary_tree import TreeNode


def inorder_traversal(root: TreeNode) -> List[int]:
    result = []

    def traversal(root: TreeNode):
        if root is None:
            return
        traversal(root.left)
        result.append(root.value)
        traversal(root.right)

    traversal(root)
    return result


def inorder_traversal_iter(root: TreeNode) -> List[int]:
    result = []
    stack = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.value)
            cur = cur.right
    return result
