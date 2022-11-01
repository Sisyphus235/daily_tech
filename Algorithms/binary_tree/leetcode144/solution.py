# -*- coding: utf8 -*-

from typing import List
from binary_tree import TreeNode


def preorder_traversal(root: TreeNode) -> List[int]:
    result = []

    def traversal(root: TreeNode):
        if root is None:
            return
        result.append(root.value)
        traversal(root.left)
        traversal(root.right)

    traversal(root)
    return result


def preorder_traversal_iter(root: TreeNode) -> List[int]:
    result = []
    iter_stack = []
    iter_stack.append(root)
    while iter_stack:
        node = iter_stack.pop()
        if node:
            result.append(node.value)
            iter_stack.append(node.right)
            iter_stack.append(node.left)
    return result
