"""
    Leetcode No: 21
    Title: Merge Two Sorted Lists
    Description:
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by
    splicing together the nodes of the first two lists.
    Return the head of the merged linked list.


    Example 1:

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:

    Input: list1 = [], list2 = []
    Output: []

    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy_node = ListNode()

        current_node = dummy_node

        while list1 and list2:

            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next

            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1:
            current_node.next = list1

        if list2:
            current_node.next = list2

        # Return dummy node's head because the current_node will be pointing
        # to the end of the list once it get out of the loop and is why we
        # cannot return it
        return dummy_node.next
