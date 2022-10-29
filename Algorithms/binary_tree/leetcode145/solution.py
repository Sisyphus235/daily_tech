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
