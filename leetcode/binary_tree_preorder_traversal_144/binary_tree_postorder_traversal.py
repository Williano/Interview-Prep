"""
    Leetcode No: 144
    Title: Binary Tree Preorder Traversal
    Description:
    Given the root of a binary tree, return the preorder traversal of its nodes' values.


    Example 1:

    Input: root = [1,null,2,3]
    Output: [1,2,3]

    Example 2:

    Input: root = []
    Output: []

    Example 3:

    Input: root = [1]
    Output: [1]
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pre_order_traversal(self, root: Optional[TreeNode]) -> List[int]:

        pre_order_traversal = []

        if root is None:
            return root

        pre_order_traversal.append(root.val)

        if root.left:
            pre_order_traversal += self.pre_order_traversal(root.left)

        if root.right:
            pre_order_traversal += self.pre_order_traversal(root.right)

        return pre_order_traversal
