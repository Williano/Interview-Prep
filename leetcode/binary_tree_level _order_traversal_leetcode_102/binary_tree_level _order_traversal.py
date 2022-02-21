"""
    Leetcode No: 102
    Title: Binary Tree Level Order Traversal
    Description:
    Given the root of a binary tree, return the level order traversal of its
    nodes' values. (i.e., from left to right, level by level).

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]


    Example 2:

    Input: root = [1]
    Output: [[1]]

    Example 3:

    Input: root = []
    Output: []
"""
import imp
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return root

        tree_queue = deque()
        tree_queue.append(root)

        level_order_traversal = []

        while tree_queue:

            tree_levels = []

            for _ in range(len(tree_queue)):

                current_node = tree_queue.popleft()

                if current_node:
                    tree_levels.append(current_node.val)

                if current_node.left:
                    tree_queue.append(current_node.left)

                if current_node.right:
                    tree_queue.append(current_node.right)

            level_order_traversal.append(tree_levels)

        return level_order_traversal
