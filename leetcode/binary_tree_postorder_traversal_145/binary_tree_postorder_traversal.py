"""
    Leetcode No: 145
    Title: Binary Tree Postorder Traversal
    Description:
    Given the root of a binary tree, return the postorder traversal of its nodes' values.


    Example 1:

    Input: root = [1,null,2,3]
    Output: [3, 2, 1]

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
    def post_order_traversal(self, root: Optional[TreeNode]) -> List[int]:

        post_order_traversal = []

        if root is None:
            return root

        # Travese left sub-tree
        if root.left:
            post_order_traversal += self.post_order_traversal(root.left)

        # Travese right sub-tree
        if root.right:
            post_order_traversal += self.post_order_traversal(root.right)

        # Add root node
        post_order_traversal.append(root.val)

        return post_order_traversal
