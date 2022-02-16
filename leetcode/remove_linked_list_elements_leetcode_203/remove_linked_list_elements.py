"""
    Leetcode No: 203

    Title: Remove Linked List Elements

    Description:
    Given the head of a linked list and an integer val, remove all the nodes of the
    linked list that has Node.val == val, and return the new head.

    Example 1:

    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]


    Example 2:

    Input: head = [], val = 1
    Output: []

    Example 3:

    Input: head = [7,7,7,7], val = 7
    Output: []
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_elements(self, head, val: int):

        if head is None:
            return head

        sentinel_node = ListNode(0)
        sentinel_node.next = head

        current_node, previous_node = sentinel_node.next, sentinel_node

        while current_node:

            if current_node.val == val:
                previous_node.next = current_node.next

            else:
                previous_node = current_node

            current_node = current_node.next

        return sentinel_node.next
