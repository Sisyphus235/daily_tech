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


def inorder_traversal_iter_uni(root: TreeNode) -> List[int]:
    result = []
    stack = []
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            stack.append(None)
            if node.left:
                stack.append(node.left)
        else:
            node = stack.pop()
            result.append(node.value)
    return result
