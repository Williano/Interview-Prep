"""
    Leetcode No: 94
    Title: Binary Tree Inorder Traversal
    Description:
    Given the root of a binary tree, return the inorder traversal of its nodes' values.


    Example 1:

    Input: root = [1,null,2,3]
    Output: [1,3,2]

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
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:

        in_order_traversal = []

        if root is None:
            return root

        # Traverse left sub-tree
        if root.left:
            in_order_traversal += self.inorder_traversal(root.left)

        # Add root node
        in_order_traversal.append(root.val)

        # Traverse right sub-tree
        if root.right:
            in_order_traversal += self.inorder_traversal(root.right)

        return in_order_traversal
