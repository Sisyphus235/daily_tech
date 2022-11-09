# -*- coding: utf8 -*-

from typing import List
from binary_tree import TreeNode


def postorder_traversal(root: TreeNode) -> List[int]:
    result = []

    def traversal(root: TreeNode):
        if root is None:
            return
        traversal(root.left)
        traversal(root.right)
        result.append(root.value)

    traversal(root)
    return result


def postorder_traversal_iter(root: TreeNode) -> List[int]:
    result = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            result.append(node.value)
            stack.append(node.left)
            stack.append(node.right)
    result.reverse()
    return result


def postorder_traversal_iter_universe(root: TreeNode) -> List[int]:
    result = []
    stack = []
    if root is not None:
        stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        else:
            node = stack.pop()
            result.append(node.value)
    return result
