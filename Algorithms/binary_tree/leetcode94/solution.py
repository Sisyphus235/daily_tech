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
