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
